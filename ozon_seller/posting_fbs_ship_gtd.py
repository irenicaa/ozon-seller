from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PostingFBSShipWithGTDAdditionalFields(DataClassJsonMixin):
    additional_data: Optional[bool] = False


@dataclass
class PostingFBSShipWithGTDExemplarInfo(DataClassJsonMixin):
    mandatory_mark: Optional[str] = None
    gtd: Optional[str] = None
    is_gtd_absent: Optional[bool] = True


@dataclass
class PostingFBSShipWithGTDProduct(DataClassJsonMixin):
    exemplar_info: Optional[list[PostingFBSShipWithGTDExemplarInfo]] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None


@dataclass
class PostingFBSShipWithGTDPackage(DataClassJsonMixin):
    products: Optional[list[PostingFBSShipWithGTDProduct]] = None


@dataclass
class PostingFBSShipWithGTDData(DataClassJsonMixin):
    packages: Optional[list[PostingFBSShipWithGTDPackage]] = None
    posting_number: Optional[str] = None
    with_: Optional[PostingFBSShipWithGTDAdditionalFields] = field(
        default=None,
        metadata=config(field_name="with"),
    )


# Response


@dataclass
class CreatePostingFBSShipWithGTDResponseResultWrapper(DataClassJsonMixin):
    result: list[str]


def create_posting_fbs_ship_with_gtd(
    credentials: credentials.Credentials,
    data: PostingFBSShipWithGTDData,
) -> CreatePostingFBSShipWithGTDResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v3/posting/fbs/ship",
        credentials,
        data,
        response_cls=CreatePostingFBSShipWithGTDResponseResultWrapper,
    )
