import datetime
from dataclasses import dataclass
from typing import Iterator, Optional

from .common import credentials, request_api, datetime_field, make_iterative
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class GetReturnsCompanyFBOFilter(DataClassJsonMixin):
    posting_number: Optional[str] = None
    status: Optional[list[str]] = None


@dataclass
class PaginatedGetReturnsCompanyFBOFilter(DataClassJsonMixin):
    filter: Optional[GetReturnsCompanyFBOFilter] = None
    offset: Optional[int] = None
    limit: Optional[int] = None


# Response


@dataclass
class GetReturnsCompanyFBOResponseItem(DataClassJsonMixin):
    company_id: int
    current_place_name: str
    dst_place_name: str
    id: int
    is_opened: bool
    posting_number: str
    return_reason_name: str
    sku: int
    status_name: str
    accepted_from_customer_moment: datetime.datetime = \
        datetime_field.datetime_field()
    returned_to_ozon_moment: datetime.datetime = datetime_field.datetime_field()


@dataclass
class GetReturnsCompanyFBOResponseResult(DataClassJsonMixin):
    returns: list[GetReturnsCompanyFBOResponseItem]
    count: int


def get_returns_company_fbo(
    credentials: credentials.Credentials,
    data: PaginatedGetReturnsCompanyFBOFilter,
) -> GetReturnsCompanyFBOResponseResult:
    return request_api.request_api_json(
        "POST",
        "/v2/returns/company/fbo",
        credentials,
        data,
        response_cls=GetReturnsCompanyFBOResponseResult,
    )


def get_returns_company_fbo_iterative(
    credentials: credentials.Credentials,
    data: PaginatedGetReturnsCompanyFBOFilter,
) -> Iterator[GetReturnsCompanyFBOResponseItem]:
    return make_iterative.make_iterative_via_offset(
        request=data,
        requester=lambda: get_returns_company_fbo(credentials, data),
        extract_response_items=lambda response: response.returns,
    )
