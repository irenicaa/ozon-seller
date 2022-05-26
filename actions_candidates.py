from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class CandidatesForActions:
    action_id: float
    limit: float
    offset: float

# Response

@dataclass_json
@dataclass
class CandidatesForActionsProducts:
    id: float
    price: float
    action_price: float
    max_action_price: float
    add_mode: str
    min_stock: float
    stock: float

@dataclass_json
@dataclass
class GetActionsCandidatesResponseResult:
    products: list[CandidatesForActionsProducts]
    total: float

@dataclass_json
@dataclass
class GetActionsCandidatesResponseResultWrapper:
    result: GetActionsCandidatesResponseResult
