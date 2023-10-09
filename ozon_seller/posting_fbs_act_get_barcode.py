from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin
from marshmallow import fields

from .common import credentials, request_api

# Request


@dataclass
class FBSActData(DataClassJsonMixin):
    id: int


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSResponseResult:
    content: bytes


def get_posting_fbs_act_barcode(
    credentials: credentials.Credentials,
    data: FBSActData,
) -> bytes:
    response = request_api.request_api_raw(
        "POST",
        "/v2/posting/fbs/act/get-barcode",
        credentials,
        data.to_json(),
    )
    return response.content
