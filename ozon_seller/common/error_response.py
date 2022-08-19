from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import Undefined, config, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ErrorResponseDetail:
    type_url: Optional[int] = field(
        default=None,
        metadata=config(field_name="typeUrl"),
    )
    value: Optional[str] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ErrorResponse:
    code: Optional[int]
    message: Optional[str]
    details: Optional[list[ErrorResponseDetail]]
