from dataclasses import dataclass, field, fields
from typing import Any

from . import qualified_name


_PRIMARY_FIELD_METADATA_KEY = "primary-field"


def primary_field() -> Any:
    return field(metadata={_PRIMARY_FIELD_METADATA_KEY: True})


@dataclass
class BaseTestCase:
    kind: str

    @property
    def name(self) -> str:
        primary_fields = tuple(
            field
            for field in fields(self)
            if field.metadata.get(_PRIMARY_FIELD_METADATA_KEY)
        )
        if len(primary_fields) == 0:
            raise ValueError("primary field is not defined")
        if len(primary_fields) > 1:
            raise ValueError("more than one primary field is defined")

        primary_field_value = getattr(self, primary_fields[0].name)
        primary_field_module = qualified_name.get_last_module(primary_field_value)
        return f"{primary_field_module} [{self.kind}]"
