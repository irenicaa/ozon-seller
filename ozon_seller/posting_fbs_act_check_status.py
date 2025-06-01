from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PostingFSBActData(DataClassJsonMixin):
    id: Optional[int] = None


# Response


@dataclass
class PostingFBSActCheckStatusResponseResult(DataClassJsonMixin):
    act_type: str
    added_to_act: list[str]
    removed_from_act: list[str]
    status: str


@dataclass
class PostingFBSActCreateResponseActResultWrapper(DataClassJsonMixin):
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
