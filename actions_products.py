from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class PaginatedActionProducts:
    action_id: Optional[float] = None
    limit: Optional[float] = None
    offset: Optional[float] = None

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

def get_action_products(
    credentials: credentials.Credentials,
    data: PaginatedActionProducts,
) -> GetSellerProductResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v1/actions/products',
        credentials,
        data.to_json(),
    )
    return GetSellerProductResponseResultWrapper.schema().loads(response)

def get_action_products_iterative(
    credentials: credentials.Credentials,
    data: PaginatedActionProducts,
) -> GetSellerProductResponseResultWrapper:
    while True:
        products = get_action_products(credentials, data)
        if products.result.products == []:
            break

        yield products

        data.offset += data.limit
