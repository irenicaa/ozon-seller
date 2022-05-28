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
class GetProductInfoDescriptionResponse:
    description: str
    id: int
    name: str
    offer_id: str

@dataclass_json
@dataclass
class GetProductInfoDescriptionResponseWrapper:
    result: GetProductInfoDescriptionResponse

def get_product_description(
    credentials: credentials.Credentials,
    data: ProductData,
) -> GetProductInfoDescriptionResponseWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v1/product/info/description',
        credentials,
        data.to_json(),
    )
    return GetProductInfoDescriptionResponseWrapper.schema().loads(response)
