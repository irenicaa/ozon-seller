from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials

# Response

@dataclass_json
@dataclass
class GetSellerActionsResponse:
    id: float
    title: str
    action_type: str
    description: str
    date_start: str
    date_end: str
    freeze_date: str
    potential_products_count: float
    participating_products_count: float
    is_participating: bool
    banned_products_count: float
    with_targeting: bool
    order_amount: float
    discount_type: str
    discount_value: float

@dataclass_json
@dataclass
class GetSellerActionsResponseWrapper:
    result: list[GetSellerActionsResponse]
