from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json

from .common import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PaginatedActionProducts:
    action_id: Optional[float] = None
    limit: Optional[float] = None
    offset: Optional[float] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetSellerProductResponseProducts:
    id: int
    price: float
    action_price: float
    max_action_price: float
    add_mode: str
    min_stock: float
    stock: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetSellerProductResponseResult:
    products: list[GetSellerProductResponseProducts]
    total: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetSellerProductResponseResultWrapper:
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
