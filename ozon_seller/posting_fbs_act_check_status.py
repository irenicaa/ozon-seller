import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json
from marshmallow import fields

from . import request_api
from .common import credentials

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFSBActData:
    id: Optional[int] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActCheckStatusResponseResult:
    act_type: str
    added_to_act: list[str]
    removed_from_act: list[str]
    status: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActCreateResponseActResultWrapper:
    result: PostingFBSActCheckStatusResponseResult


def create_posting_fbs_act(
    credentials: credentials.Credentials,
    data: PostingFSBActData,
) -> PostingFBSActCreateResponseActResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/posting/fbs/act/check-status",
        credentials,
        data,
        response_cls=PostingFBSActCreateResponseActResultWrapper,
    )
