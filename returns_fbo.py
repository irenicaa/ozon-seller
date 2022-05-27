from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, config
from typing import Optional
from marshmallow import fields

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class GetReturnsCompanyFboRequestFilter:
    posting_number: Optional[str] = None
    status: Optional[list[str]] = None

@dataclass_json
@dataclass
class GetReturnsCompanyFboRequest:
    filter: Optional[GetReturnsCompanyFboRequestFilter] = None
    offset: Optional[int] = None
    limit: Optional[int] = None

# Response

@dataclass_json
@dataclass
class GetReturnsCompanyFboResponse:
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
class GetReturnsCompanyFboResponseWrapper:
    count: int
    returns: list[GetReturnsCompanyFboRequest]

def get_returns_company_fbo(
    credentials: credentials.Credentials,
    data: GetReturnsCompanyFboRequest,
) -> GetReturnsCompanyFboResponseWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v2/returns/company/fbo',
        credentials,
        data.to_json(),
    )
    return GetReturnsCompanyFboResponseWrapper.schema().loads(response)
