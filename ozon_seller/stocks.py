from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json

from .common import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductFilter:
    offer_id: Optional[list[str]] = None
    product_id: Optional[list[str]] = None
    visibility: Optional[list[str]] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PaginatedProductFilter:
    filter: ProductFilter
    last_id: str
    limit: int


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoStocksResponseStock:
    present: int
    reserved: int
    type: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoStocksResponseItem:
    offer_id: str
    product_id: int
    stocks: list[GetProductInfoStocksResponseStock]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoStocksResponseResult:
    items: list[GetProductInfoStocksResponseItem]
    last_id: str
    total: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoStocksResponseResultWrapper:
    result: GetProductInfoStocksResponseResult


def get_product_info_stocks(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> GetProductInfoStocksResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v3/product/info/stocks",
        credentials,
        data,
        response_cls=GetProductInfoStocksResponseResultWrapper,
    )


def get_product_info_stocks_iterative(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> Generator[GetProductInfoStocksResponseResultWrapper, None, None]:
    while True:
        stocks = get_product_info_stocks(credentials, data)
        if stocks.result.items == []:
            break

        yield stocks

        data.last_id = stocks.result.last_id
