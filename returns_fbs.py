from dataclasses import dataclass

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class ProductFilter:
    filter: returnsGetReturnsCompanyFBSRequestFilter
    limit: int
    offset: int

@dataclass_json
@dataclass
class returnsGetReturnsCompanyFBSRequestFilter:
    accepted_from_customer_moment: list[FilterTimeRange]
    last_free_waiting_day: list[FilterTimeRange]
    order_id: int
    posting_number: list[str]
    product_name: str
    product_offer_id: str
    status: str

# TODO: time type
@dataclass_json
@dataclass
class FilterTimeRange:
    time_from: str
    time_to: str
