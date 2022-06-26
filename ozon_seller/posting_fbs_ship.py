import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

from . import credentials, request_api, returns_fbs

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
        "POST",
        "/v2/posting/fbs/ship",
        credentials,
        data.to_json(),
    )
    return PostingFBSShipResponseResult.schema().loads(response)
