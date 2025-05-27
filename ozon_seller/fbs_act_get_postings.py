from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api, datetime_field

# Request


@dataclass
class PostingFBSActData(DataClassJsonMixin):
    id: Optional[int] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActDataResponseProducts:
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActDataResponseResult:
    id: int
    multi_box_qty: int
    posting_number: str
    status: str
    seller_error: str
    updated_at: str
    created_at: str
    products: list[PostingFBSActDataResponseProducts]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PostingFBSActDataResponseResultWrapper:
    result: list[PostingFBSActDataResponseResult]


def get_posting_fbs_act_data(
    credentials: credentials.Credentials,
    data: PostingFBSActData,
) -> PostingFBSActDataResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/posting/fbs/act/get-postings",
        credentials,
        data,
        response_cls=PostingFBSActDataResponseResultWrapper,
    )
