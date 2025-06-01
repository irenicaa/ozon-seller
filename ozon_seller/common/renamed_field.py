import dataclasses
from typing import TypeVar, Optional, cast

import dataclasses_json


T = TypeVar("T")


def _base_renamed_field(
    cls: type[T],
    new_name: str,
    is_optional: bool,
) -> Optional[T]:
    return dataclasses.field(
        default=cast(Optional[T], None if is_optional else dataclasses.MISSING),
        metadata=dataclasses_json.config(field_name=new_name),
    )


def renamed_field(cls: type[T], new_name: str) -> T:
    field = _base_renamed_field(cls, new_name, is_optional=False)
    assert field is not None

    return field


def optional_renamed_field(cls: type[T], new_name: str) -> Optional[T]:
    return _base_renamed_field(cls, new_name, is_optional=True)
