from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials
import returns_fbs

# Request

@dataclass_json
@dataclass
class PostingFBSShipWithGTDAdditionalFields:
    additional_data: Optional[bool] = False

@dataclass_json
@dataclass
class PostingFBSShipWithGTDExemplarInfo:
    mandatory_mark: Optional[str] = None
    gtd: Optional[str] = None
    is_gtd_absent: Optional[bool] = True

@dataclass_json
@dataclass
class PostingFBSShipWithGTDProduct:
    exemplar_info: Optional[list[PostingFBSShipWithGTDExemplarInfo]] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None

@dataclass_json
@dataclass
class PostingFBSShipWithGTDPackage:
    products: Optional[list[PostingFBSShipWithGTDProduct]] = None

@dataclass_json
@dataclass
class PostingFBSShipWithGTDData:
    packages: Optional[list[PostingFBSShipWithGTDPackage]] = None
    posting_number: Optional[str] = None
    with_: Optional[PostingFBSShipWithGTDAdditionalFields] = field(
        default=None,
        metadata=config(field_name="with"),
    )

# Response

@dataclass_json
@dataclass
class CreatePostingFBSShipWithGTDResponseResultWrapper:
    result: list[str]

def create_posting_fbs_ship_with_gtd(
    credentials: credentials.Credentials,
    data: PostingFBSShipWithGTDData,
) -> CreatePostingFBSShipWithGTDResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v3/posting/fbs/ship',
        credentials,
        data.to_json(),
    )
    return CreatePostingFBSShipWithGTDResponseResultWrapper.schema().loads(response)
