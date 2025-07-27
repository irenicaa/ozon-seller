import datetime
from dataclasses import dataclass, field
from typing import Iterator, Optional

from .common import credentials, request_api, datetime_field, make_iterative
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class FilterTimeRange(DataClassJsonMixin):
    time_from: datetime.datetime = datetime_field.datetime_field()
    time_to: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetReturnsCompanyFBSFilter(DataClassJsonMixin):
    accepted_from_customer_moment: Optional[list[FilterTimeRange]] = None
    last_free_waiting_day: Optional[list[FilterTimeRange]] = None
    order_id: Optional[int] = None
    posting_number: list[str] = field(default_factory=list)
    product_name: str = ""
    product_offer_id: str = ""
    status: str = ""


@dataclass
class PaginatedGetReturnsCompanyFBSFilter(DataClassJsonMixin):
    filter: GetReturnsCompanyFBSFilter
    offset: int
    limit: int


# Response


@dataclass
class GetReturnsCompanyFBSResponseItem(DataClassJsonMixin):
    accepted_from_customer_moment: Optional[str]
    clearing_id: Optional[int]
    commission: Optional[float]
    commission_percent: Optional[float]
    id: Optional[int]
    is_moving: Optional[bool]
    is_opened: Optional[bool]
    last_free_waiting_day: Optional[str]
    place_id: Optional[int]
    moving_to_place_name: Optional[str]
    picking_amount: Optional[float]
    posting_number: Optional[str]
    price: Optional[float]
    price_without_commission: Optional[float]
    product_id: Optional[int]
    product_name: Optional[str]
    quantity: Optional[int]
    return_date: Optional[str]
    return_reason_name: Optional[str]
    waiting_for_seller_date_time: Optional[str]
    returned_to_seller_date_time: Optional[str]
    waiting_for_seller_days: Optional[int]
    returns_keeping_cost: Optional[float]
    sku: Optional[int]
    status: Optional[str]


@dataclass
class GetReturnsCompanyFBSResponseResult(DataClassJsonMixin):
    returns: list[GetReturnsCompanyFBSResponseItem]
    count: int


@dataclass
class GetReturnsCompanyFBSResponseResultWrapper(DataClassJsonMixin):
    result: GetReturnsCompanyFBSResponseResult


def get_returns_company_fbs(
    credentials: credentials.Credentials,
    data: PaginatedGetReturnsCompanyFBSFilter,
) -> GetReturnsCompanyFBSResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v2/returns/company/fbs",
        credentials,
        data,
        response_cls=GetReturnsCompanyFBSResponseResultWrapper,
    )


def get_returns_company_fbs_iterative(
    credentials: credentials.Credentials,
    data: PaginatedGetReturnsCompanyFBSFilter,
) -> Iterator[GetReturnsCompanyFBSResponseItem]:
    return make_iterative.make_iterative_via_offset(
        request=data,
        requester=lambda: get_returns_company_fbs(credentials, data),
        extract_response_items=lambda response: response.result.returns,
    )
