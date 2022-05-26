from dataclasses import dataclass

from dataclasses_json import dataclass_json

import request_api
import credentials

# Request

@dataclass_json
@dataclass
class ActionProducts:
    action_id: float
    limit: float
    offset: float
