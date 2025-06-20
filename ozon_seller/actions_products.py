from dataclasses import dataclass
from typing import Generator, Optional

from .common import credentials, request_api
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
) -> Generator[GetSellerProductResponseResultWrapper, None, None]:
    while True:
        products = get_action_products(credentials, data)
        if products.result.products == []:
            break

        yield products

        data.offset += data.limit
