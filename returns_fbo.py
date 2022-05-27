from dataclasses import dataclass
from typing import Optional
import datetime

from dataclasses_json import dataclass_json

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
