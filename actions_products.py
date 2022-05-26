from dataclasses import dataclass

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class ActionProducts:
    action_id: float
    limit: float
    offset: float

# Response

@dataclass_json
@dataclass
class GetSellerProductResponseProducts:
    id: int
    price: float
    action_price: float
    max_action_price: float
    add_mode: str
    min_stock: float
    stock: float


@dataclass_json
@dataclass
class GetSellerProductResponseResult:
    products: list[GetSellerProductResponseProducts]
    total: int

@dataclass_json
@dataclass
class GetSellerProductResponseResultWrapper:
    result: GetSellerProductResponseResult
