from dataclasses import dataclass
from dataclasses import field

from dataclasses_json import dataclass_json
from typing import Optional

import request_api
import credentials

# Request


# TODO: time type
@dataclass_json
@dataclass
class FilterTimeRange:
    time_from: str
    time_to: str

@dataclass_json
@dataclass
class returnsGetReturnsCompanyFBSRequestFilter:
    accepted_from_customer_moment: Optional[list[FilterTimeRange]]
    last_free_waiting_day: Optional[list[FilterTimeRange]]
    order_id: Optional[int] = None
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

@dataclass_json
@dataclass
class ResultGetReturnsCompanyFBSItem:
    accepted_from_customer_moment: str
    clearing_id: int
    commission: float
    commission_percent: float
    id: int
    is_moving: bool
    is_opened: bool
    last_free_waiting_day: str
    place_id: int
    moving_to_place_name: str
    picking_amount: float
    posting_number: str
    price: float
    price_without_commission: float
    product_id: int
    product_name: str
    quantity: int
    return_date: str
    return_reason_name: str
    waiting_for_seller_date_time: str
    returned_to_seller_date_time: str
    waiting_for_seller_days: int
    returns_keeping_cost: float
    sku: int
    status: str

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
