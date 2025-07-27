from dataclasses import dataclass
from typing import Iterator, Optional

from .common import credentials, request_api, make_iterative
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PaginatedActionProducts(DataClassJsonMixin):
    action_id: Optional[float] = None
    limit: Optional[float] = None
    offset: Optional[float] = None


# Response


@dataclass
class GetSellerProductResponseProducts(DataClassJsonMixin):
    id: int
    price: float
    action_price: float
    max_action_price: float
    add_mode: str
    min_stock: float
    stock: float


@dataclass
class GetSellerProductResponseResult(DataClassJsonMixin):
    products: list[GetSellerProductResponseProducts]
    total: int


@dataclass
class GetSellerProductResponseResultWrapper(DataClassJsonMixin):
    result: GetSellerProductResponseResult


def get_action_products(
    credentials: credentials.Credentials,
    data: PaginatedActionProducts,
) -> GetSellerProductResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v1/actions/products",
        credentials,
        data,
        response_cls=GetSellerProductResponseResultWrapper,
    )


def get_action_products_iterative(
    credentials: credentials.Credentials,
    data: PaginatedActionProducts,
) -> Iterator[GetSellerProductResponseResultWrapper]:
    def _shift_request(response: GetSellerProductResponseResultWrapper) -> None:
        nonlocal data

        previous_offset = data.offset if data.offset is not None else 0
        data.offset = previous_offset + len(response.result.products)

    return make_iterative.make_iterative(
        requester=lambda: get_action_products(credentials, data),
        get_response_length=lambda response: len(response.result.products),
        shift_request=_shift_request,
    )
