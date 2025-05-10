from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class ProductsStocksList(DataClassJsonMixin):
    offer_id: str
    product_id: int
    stock: int
    warehouse_id: int


@dataclass
class ProductImportProductsStocks(DataClassJsonMixin):
    stocks: list[ProductsStocksList]


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductImportProductsStocksResponseError:
    code: str
    message: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductsStocksResponseProcessResult:
    errors: list[ProductImportProductsStocksResponseError]
    offer_id: str
    product_id: int
    updated: bool
    warehouse_id: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductsStocksResponseProcessResultWrapper:
    result: list[ProductsStocksResponseProcessResult]


def set_stocks(
    credentials: credentials.Credentials,
    data: ProductImportProductsStocks,
) -> ProductsStocksResponseProcessResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/products/stocks",
        credentials,
        data,
        response_cls=ProductsStocksResponseProcessResultWrapper,
    )
