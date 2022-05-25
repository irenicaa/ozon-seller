from dataclasses import dataclass, field
from typing import Optional
import datetime

from dataclasses_json import dataclass_json, Undefined, config

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class ProductData:
    offer_id: str
    product_id: int
    sku: int
