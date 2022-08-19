import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import Undefined, config, dataclass_json
from marshmallow import fields

from . import request_api
from .common import credentials

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetReturnsCompanyFBOFilter:
    posting_number: Optional[str] = None
    status: Optional[list[str]] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class PaginatedGetReturnsCompanyFBOFilter:
    filter: Optional[GetReturnsCompanyFBOFilter] = None
    offset: Optional[int] = None
    limit: Optional[int] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetReturnsCompanyFBOResponseItem:
    accepted_from_customer_moment: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
    )
    company_id: int
    current_place_name: str
    dst_place_name: str
    id: int
    is_opened: bool
    posting_number: str
    return_reason_name: str
    returned_to_ozon_moment: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format="iso"),
        ),
    )
    sku: int
    status_name: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetReturnsCompanyFBOResponseResult:
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
) -> Generator[GetReturnsCompanyFBOResponseResult, None, None]:
    while True:
        returns = get_returns_company_fbo(credentials, data)
        if returns.returns == []:
            break

        yield returns

        data.offset += data.limit
