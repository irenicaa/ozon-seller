from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class ProductFilterWithQuant(DataClassJsonMixin):
    created: Optional[bool] = None


@dataclass
class ProductFilter(DataClassJsonMixin):
    offer_id: Optional[list[str]] = None
    product_id: Optional[list[str]] = None
    visibility: Optional[str] = None
    with_quant: Optional[ProductFilterWithQuant] = None


@dataclass
class PaginatedProductFilter(DataClassJsonMixin):
    filter: ProductFilter
    cursor: str
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
    cursor: str
    items: list[GetProductInfoStocksResponseItem]
    total: int


def get_product_info_stocks(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> GetProductInfoStocksResponseResult:
    return request_api.request_api_json(
        "POST",
        "/v4/product/info/stocks",
        credentials,
        data,
        response_cls=GetProductInfoStocksResponseResult,
    )


def get_product_info_stocks_iterative(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> Generator[GetProductInfoStocksResponseResult, None, None]:
    while True:
        stocks = get_product_info_stocks(credentials, data)
        if stocks.cursor == "":
            break

        yield stocks

        data.cursor = stocks.cursor
