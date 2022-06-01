from dataclasses import dataclass
from typing import Optional
import datetime

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class ProductData:
    offer_id: Optional[str] = None
    product_id: Optional[int] = None

# Response

@dataclass_json
@dataclass
class GetProductInfoDescriptionResponseResult:
    description: str
    id: int
    name: str
    offer_id: str

@dataclass_json
@dataclass
class GetProductInfoDescriptionResponseResultWrapper:
    result: GetProductInfoDescriptionResponseResult

def get_product_description(
    credentials: credentials.Credentials,
    data: ProductData,
) -> GetProductInfoDescriptionResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v1/product/info/description',
        credentials,
        data.to_json(),
    )
    return GetProductInfoDescriptionResponseResultWrapper.schema().loads(response)
