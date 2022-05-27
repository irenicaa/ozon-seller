from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, config
from marshmallow import fields

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class GetReturnsCompanyFboRequestFilter:
    posting_number: str
    status: list[str]

@dataclass_json
@dataclass
class GetReturnsCompanyFboRequest:
    filter: GetReturnsCompanyFboRequestFilter
    offset: int
    limit: int

# Response

@dataclass_json
@dataclass
class ReturnsCompanyFboResponse:
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
class ReturnsCompanyFboResponseWrapper:
    count: int
    returns: list[ReturnsCompanyFboResponse]
