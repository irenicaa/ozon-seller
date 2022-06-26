import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

import credentials
import request_api


def format_datetime(value):
    return value.astimezone(datetime.timezone.utc).isoformat(timespec="microseconds")


# Request


@dataclass_json
@dataclass
class PostingFSBDeliveryData:
    containers_count: Optional[int] = None
    delivery_method_id: Optional[int] = None
    departure_date: Optional[datetime.datetime] = field(
        metadata=config(encoder=format_datetime),
        default=None,
    )


# Response


@dataclass_json
@dataclass
class PostingFBSActCreateResponseActResult:
    id: int


@dataclass_json
@dataclass
class PostingFBSActCreateResponseActResultWrapper:
    result: PostingFBSActCreateResponseActResult


def create_posting_fbs_act(
    credentials: credentials.Credentials,
    data: PostingFSBDeliveryData,
) -> PostingFBSActCreateResponseActResultWrapper:
    response = request_api.request_api_raw(
        "POST",
        "/v2/posting/fbs/act/create",
        credentials,
        data.to_json(),
    )
    return PostingFBSActCreateResponseActResultWrapper.schema().loads(response)
