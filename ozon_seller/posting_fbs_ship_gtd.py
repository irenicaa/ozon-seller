import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

from . import credentials, request_api, returns_fbs

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSShipWithGTDAdditionalFields:
    additional_data: Optional[bool] = False


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSShipWithGTDExemplarInfo:
    mandatory_mark: Optional[str] = None
    gtd: Optional[str] = None
    is_gtd_absent: Optional[bool] = True


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSShipWithGTDProduct:
    exemplar_info: Optional[list[PostingFBSShipWithGTDExemplarInfo]] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSShipWithGTDPackage:
    products: Optional[list[PostingFBSShipWithGTDProduct]] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSShipWithGTDData:
    packages: Optional[list[PostingFBSShipWithGTDPackage]] = None
    posting_number: Optional[str] = None
    with_: Optional[PostingFBSShipWithGTDAdditionalFields] = field(
        default=None,
        metadata=config(field_name="with"),
    )


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class CreatePostingFBSShipWithGTDResponseResultWrapper:
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
