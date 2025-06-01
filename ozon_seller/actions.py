from dataclasses import dataclass

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Response


@dataclass
class GetSellerActionsResponseResult(DataClassJsonMixin):
    id: float
    title: str
    action_type: str
    description: str
    date_start: str
    date_end: str
    freeze_date: str
    potential_products_count: float
    participating_products_count: float
    is_participating: bool
    banned_products_count: float
    with_targeting: bool
    order_amount: float
    discount_type: str
    discount_value: float
    is_voucher_action: bool


@dataclass
class GetSellerActionsResponseResultWrapper(DataClassJsonMixin):
    result: list[GetSellerActionsResponseResult]


def get_actions(
    credentials: credentials.Credentials,
) -> GetSellerActionsResponseResultWrapper:
    return request_api.request_api_json(
        "GET",
        "/v1/actions",
        credentials,
        None,
        response_cls=GetSellerActionsResponseResultWrapper,
    )
