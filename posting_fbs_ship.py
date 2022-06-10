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
class FBSPackageItem:
    mandatory_mark: Optional[list[str]] = None
    quantity: Optional[int] = 1
    sku: Optional[int] = None

@dataclass_json
@dataclass
class PostingShipRequestPackages:
    items: Optional[list[FBSPackageItem]] = None

@dataclass_json
@dataclass
class FBSPostingShipRequestWith:
    additional_data: Optional[bool] = False

@dataclass_json
@dataclass
class PostingFBSShip:
    packages: Optional[list[PostingShipRequestPackages]] = None
    posting_number: Optional[str] = None

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
        '/v2/posting/fbs/ship',
        credentials,
        data.to_json(),
    )
    return PostingFBSShipResponseResult.schema().loads(response)
