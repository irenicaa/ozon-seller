import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import (
    CatchAll,
    Undefined,
    config,
    dataclass_json,
    DataClassJsonMixin,
)
from marshmallow import fields

from .common import credentials, request_api, datetime_field


# Request


@dataclass
class PostingFSBDeliveryData(DataClassJsonMixin):
    containers_count: Optional[int] = None
    delivery_method_id: Optional[int] = None
    departure_date: Optional[
        datetime.datetime
    ] = datetime_field.optional_datetime_field()


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActCreateResponseActResult:
    id: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActCreateResponseActResultWrapper:
    result: PostingFBSActCreateResponseActResult


def create_posting_fbs_act(
    credentials: credentials.Credentials,
    data: PostingFSBDeliveryData,
) -> PostingFBSActCreateResponseActResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/posting/fbs/act/create",
        credentials,
        data,
        response_cls=PostingFBSActCreateResponseActResultWrapper,
    )
