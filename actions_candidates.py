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
