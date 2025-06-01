from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config

from .data_class_json_mixin import DataClassJsonMixin


@dataclass
class ErrorResponseDetail(DataClassJsonMixin):
    type_url: Optional[int] = field(
        default=None,
        metadata=config(field_name="typeUrl"),
    )
    value: Optional[str] = None


@dataclass
class ErrorResponse(DataClassJsonMixin):
    code: Optional[int]
    message: Optional[str]
    details: Optional[list[ErrorResponseDetail]]
