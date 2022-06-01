from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json, config
from typing import Optional
from marshmallow import fields

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class GetReturnsCompanyFBOFilter:
    posting_number: Optional[str] = None
    status: Optional[list[str]] = None

@dataclass_json
@dataclass
class PaginatedGetReturnsCompanyFBOFilter:
    filter: Optional[GetReturnsCompanyFBOFilter] = None
    offset: Optional[int] = None
    limit: Optional[int] = None

# Response

@dataclass_json
@dataclass
class GetReturnsCompanyFBOResponseItem:
    accepted_from_customer_moment: datetime.datetime = field(
        metadata=config(
            decoder=datetime.datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso'),
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
            mm_field=fields.DateTime(format='iso'),
        ),
    )
    sku: int
    status_name: str

@dataclass_json
@dataclass
class GetReturnsCompanyFBOResponseResult:
    returns: list[GetReturnsCompanyFBOResponseItem]
    count: int

def get_returns_company_fbo(
    credentials: credentials.Credentials,
    data: PaginatedGetReturnsCompanyFBOFilter,
) -> GetReturnsCompanyFBOResponseResult:
    response = request_api.request_api_raw(
        'POST',
        '/v2/returns/company/fbo',
        credentials,
        data.to_json(),
    )
    return GetReturnsCompanyFBOResponseResult.schema().loads(response)

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
