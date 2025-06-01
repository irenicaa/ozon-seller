from dataclasses import dataclass

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


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


@dataclass
class ProductImportProductsStocksResponseError(DataClassJsonMixin):
    code: str
    message: str


@dataclass
class ProductsStocksResponseProcessResult(DataClassJsonMixin):
    errors: list[ProductImportProductsStocksResponseError]
    offer_id: str
    product_id: int
    updated: bool
    warehouse_id: int


@dataclass
class ProductsStocksResponseProcessResultWrapper(DataClassJsonMixin):
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
