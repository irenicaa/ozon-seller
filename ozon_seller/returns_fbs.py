import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import (
    Undefined,
    config,
    dataclass_json,
    DataClassJsonMixin,
)

from .common import credentials, request_api, datetime_field


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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetReturnsCompanyFBSResponseItem:
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetReturnsCompanyFBSResponseResult:
    returns: list[GetReturnsCompanyFBSResponseItem]
    count: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetReturnsCompanyFBSResponseResultWrapper:
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
) -> Generator[GetReturnsCompanyFBSResponseResultWrapper, None, None]:
    while True:
        returns = get_returns_company_fbs(credentials, data)
        if returns.result.returns == []:
            break

        yield returns

        data.offset += data.limit
