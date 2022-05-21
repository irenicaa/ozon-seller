from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

# Request

@dataclass_json
@dataclass
class ProductFilter:
    offer_id: List[str]
    product_id: List[str]
    visibility: str

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
    stocks: GetProductInfoStocksResponseStock

@dataclass_json
@dataclass
class GetProductInfoStocksResponseResult:
    items: List[GetProductInfoStocksResponseItem]
    last_id: str
    total: int

@dataclass_json
@dataclass
class GetProductInfoStocksResponseResultWrapper:
    result: GetProductInfoStocksResponseResult
