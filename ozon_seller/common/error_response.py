from dataclasses import dataclass
from typing import Optional

from .data_class_json_mixin import DataClassJsonMixin
from .renamed_field import optional_renamed_field


@dataclass
class ErrorResponseDetail(DataClassJsonMixin):
    type_url: Optional[str] = optional_renamed_field(str, "typeUrl")
    value: Optional[str] = None


@dataclass
class ErrorResponse(DataClassJsonMixin):
    code: Optional[int]
    message: Optional[str]
    details: Optional[list[ErrorResponseDetail]] = None
