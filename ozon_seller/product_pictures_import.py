from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class ProductPictures(DataClassJsonMixin):
    color_image: Optional[str] = None
    images: Optional[list[str]] = None
    images360: Optional[list[str]] = None
    product_id: Optional[int] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductPicturesResponseResultPictures:
    is_360: bool
    is_color: bool
    is_primary: bool
    product_id: int
    state: str
    url: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductPicturesResponseResult:
    pictures: list[ProductPicturesResponseResultPictures]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ProductPicturesResponseResultWrapper:
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
