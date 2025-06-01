import datetime
from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api, datetime_field
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PostingFSBDeliveryData(DataClassJsonMixin):
    containers_count: Optional[int] = None
    delivery_method_id: Optional[int] = None
    departure_date: Optional[datetime.datetime] = \
        datetime_field.optional_datetime_field()


# Response


@dataclass
class PostingFBSActCreateResponseActResult(DataClassJsonMixin):
    id: int


@dataclass
class PostingFBSActCreateResponseActResultWrapper(DataClassJsonMixin):
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
