from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import config

from .data_class_json_mixin import DataClassJsonMixin
from .renamed_field import optional_renamed_field


@dataclass
class ErrorResponseDetail(DataClassJsonMixin):
    type_url: Optional[int] = optional_renamed_field(int, "typeUrl")
    value: Optional[str] = None


@dataclass
class ErrorResponse(DataClassJsonMixin):
    code: Optional[int]
    message: Optional[str]
    details: Optional[list[ErrorResponseDetail]]
