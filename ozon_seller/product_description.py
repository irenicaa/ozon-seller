import datetime
from dataclasses import dataclass
from typing import Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class ProductData(DataClassJsonMixin):
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
    return request_api.request_api_json(
        "POST",
        "/v1/product/info/description",
        credentials,
        data,
        response_cls=GetProductInfoDescriptionResponseResultWrapper,
    )
