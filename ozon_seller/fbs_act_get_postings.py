from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class PostingFBSActData(DataClassJsonMixin):
    id: Optional[int] = None


# Response


@dataclass
class PostingFBSActDataResponseProducts(DataClassJsonMixin):
    name: str
    offer_id: str
    price: str
    quantity: int
    sku: int


@dataclass
class PostingFBSActDataResponseResult(DataClassJsonMixin):
    id: int
    multi_box_qty: int
    posting_number: str
    status: str
    seller_error: str
    updated_at: str
    created_at: str
    products: list[PostingFBSActDataResponseProducts]


@dataclass
class PostingFBSActDataResponseResultWrapper(DataClassJsonMixin):
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
