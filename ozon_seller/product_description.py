import datetime
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import Undefined, dataclass_json

from . import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductData:
    offer_id: Optional[str] = None
    product_id: Optional[int] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoDescriptionResponseResult:
    description: str
    id: int
    name: str
    offer_id: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductInfoDescriptionResponseResultWrapper:
    result: GetProductInfoDescriptionResponseResult


def get_product_description(
    credentials: credentials.Credentials,
    data: ProductData,
) -> GetProductInfoDescriptionResponseResultWrapper:
    response = request_api.request_api_raw(
        "POST",
        "/v1/product/info/description",
        credentials,
        data.to_json(),
    )
    return GetProductInfoDescriptionResponseResultWrapper.schema().loads(response)
