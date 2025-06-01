from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ProductPictures(DataClassJsonMixin):
    color_image: Optional[str] = None
    images: Optional[list[str]] = None
    images360: Optional[list[str]] = None
    product_id: Optional[int] = None


# Response


@dataclass
class ProductPicturesResponseResultPictures(DataClassJsonMixin):
    is_360: bool
    is_color: bool
    is_primary: bool
    product_id: int
    state: str
    url: str


@dataclass
class ProductPicturesResponseResult(DataClassJsonMixin):
    pictures: list[ProductPicturesResponseResultPictures]


@dataclass
class ProductPicturesResponseResultWrapper(DataClassJsonMixin):
    result: ProductPicturesResponseResult


def send_product_pictures(
    credentials: credentials.Credentials,
    data: ProductPictures,
) -> ProductPicturesResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v1/product/pictures/import",
        credentials,
        data,
        response_cls=ProductPicturesResponseResultWrapper,
    )
