from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class ProductFilter:
    offer_id: Optional[list[str]] = None
    product_id: Optional[list[str]] = None
    visibility: Optional[list[str]] = None

@dataclass_json
@dataclass
class PaginatedProductFilter:
    filter: ProductFilter
    last_id: str
    limit: int

# Response

@dataclass_json
@dataclass
class GetProductInfoStocksResponseStock:
    present: int
    reserved: int
    type: str

@dataclass_json
@dataclass
class GetProductInfoStocksResponseItem:
    offer_id: str
    product_id: int
    stocks: list[GetProductInfoStocksResponseStock]

@dataclass_json
@dataclass
class GetProductInfoStocksResponseResult:
    items: list[GetProductInfoStocksResponseItem]
    last_id: str
    total: int

@dataclass_json
@dataclass
class GetProductInfoStocksResponseResultWrapper:
    result: GetProductInfoStocksResponseResult

def get_product_info_stocks(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> GetProductInfoStocksResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v3/product/info/stocks',
        credentials,
        data.to_json(),
    )
    return GetProductInfoStocksResponseResultWrapper.schema().loads(response)

def get_product_info_stocks_iterative(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> GetProductInfoStocksResponseResultWrapper:
    while True:
        stocks = get_product_info_stocks(credentials, data)
        if stocks.result.items == []:
            break

        yield stocks

        data.last_id = stocks.result.last_id
