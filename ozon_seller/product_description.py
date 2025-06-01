from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ProductData(DataClassJsonMixin):
    offer_id: Optional[str] = None
    product_id: Optional[int] = None


# Response


@dataclass
class GetProductInfoDescriptionResponseResult(DataClassJsonMixin):
    description: str
    id: int
    name: str
    offer_id: str


@dataclass
class GetProductInfoDescriptionResponseResultWrapper(DataClassJsonMixin):
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
