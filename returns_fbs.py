from dataclasses import dataclass
from dataclasses import field
import datetime

from dataclasses_json import dataclass_json
from dataclasses_json import config
from typing import Optional
from dataclasses_json import Undefined

import request_api
import credentials

# Request


# TODO: time type
@dataclass_json
@dataclass
class FilterTimeRange:
    time_from: datetime.datetime = field(metadata=config(encoder=lambda value:  value.astimezone(datetime.timezone.utc).isoformat(timespec='microseconds')))
    time_to: datetime.datetime = field(metadata=config(encoder=lambda value: value.astimezone(datetime.timezone.utc).isoformat(timespec='microseconds')))
@dataclass_json
@dataclass
class returnsGetReturnsCompanyFBSRequestFilter:
    accepted_from_customer_moment: Optional[list[FilterTimeRange]]
    last_free_waiting_day: Optional[list[FilterTimeRange]]
    order_id: Optional[int]=None
    posting_number: list[str]=field(default_factory=list)
    product_name: str = ''
    product_offer_id: str = ''
    status: str = ''

@dataclass_json
@dataclass
class ProductFilter:
    filter: returnsGetReturnsCompanyFBSRequestFilter
    limit: int
    offset: int

# Response

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ResultGetReturnsCompanyFBSItem:
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

@dataclass_json
@dataclass
class GetReturnsCompanyFBSResponseResult:
    count: int
    returns: list[ResultGetReturnsCompanyFBSItem]

@dataclass_json
@dataclass
class returnsGetReturnsCompanyFBSResponse:
    result: GetReturnsCompanyFBSResponseResult

def get_returns_from_fbs(
    credentials: credentials.Credentials,
    data: ProductFilter,
) -> returnsGetReturnsCompanyFBSResponse:
    response = request_api.request_api_raw(
        'POST',
        '/v2/returns/company/fbs',
        credentials,
        data.to_json(),
    )
    return returnsGetReturnsCompanyFBSResponse.schema().loads(response)

def get_returns_from_fbs_iterative(
    credentials: credentials.Credentials,
    data: ProductFilter,
) -> returnsGetReturnsCompanyFBSResponse:
    while True:
        returns = get_returns_from_fbs(credentials, data)
        if returns.result.count < data.limit:
            break

        yield returns

        data.offset += data.limit
