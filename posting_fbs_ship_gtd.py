from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials
import returns_fbs

# Request

@dataclass
class FBSProductExemplarInfo:
    mandatory_mark: Optional[str] = None
    gtd: Optional[str] = None
    is_gtd_absent: Optional[bool] = True

@dataclass_json
@dataclass
class FBSPackageProducts:
    exemplar_info: Optional[list[FBSProductExemplarInfo]] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None

@dataclass_json
@dataclass
class PostingShipRequestPackages:
    products: Optional[list[FBSPackageProducts]] = None

@dataclass_json
@dataclass
class FBSPostingShipRequestWith:
    additional_data: Optional[bool] = False

@dataclass_json
@dataclass
class PostingFBSShip:
    packages: Optional[list[PostingShipRequestPackages]] = None
    posting_number: Optional[str] = None
    with_: Optional[FBSPostingShipRequestWith] = field(
        default=None,
        metadata=config(field_name="with"),
    )

# Response

@dataclass_json
@dataclass
class PostingFBSShipResponseResult:
    result: list[str]

def posting_fbs_ship(
    credentials: credentials.Credentials,
    data: PostingFBSShip,
) -> PostingFBSShipResponseResult:
    response = request_api.request_api_raw(
        'POST',
        '/v3/posting/fbs/ship',
        credentials,
        data.to_json(),
    )
    return PostingFBSShipResponseResult.schema().loads(response)
