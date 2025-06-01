import dataclasses
import datetime
from typing import Optional, Union, cast

import dataclasses_json
import marshmallow.fields


def _parse_datetime(
    value: Union[None, str, datetime.datetime],
) -> Optional[datetime.datetime]:
    if value is None:
        return None
    elif isinstance(value, str):
        return datetime.datetime.fromisoformat(value)
    elif isinstance(value, datetime.datetime):
        return value
    else:
        raise RuntimeError(
            f"unsupported type {type(value)!r} for a datetime parsing",
        )


def _format_datetime(value: Optional[datetime.datetime]) -> Optional[str]:
    if value is None:
        return None
    elif isinstance(value, datetime.datetime):
        utc_value = value.astimezone(datetime.timezone.utc)
        return utc_value.isoformat(timespec="microseconds")
    else:
        raise RuntimeError(
            f"unsupported type {type(value)!r} for a datetime formatting",
        )


def _base_datetime_field(is_optional: bool) -> Optional[datetime.datetime]:
    return dataclasses.field(
        default=cast(
            Optional[datetime.datetime],
            None if is_optional else dataclasses.MISSING,
        ),
        metadata=dataclasses_json.config(
            decoder=_parse_datetime,
            encoder=_format_datetime,
            mm_field=marshmallow.fields.DateTime(
                format="iso",
                allow_none=is_optional,
            ),
        ),
    )


def datetime_field() -> datetime.datetime:
    field = _base_datetime_field(is_optional=False)
    assert field is not None

    return field


def optional_datetime_field() -> Optional[datetime.datetime]:
    return _base_datetime_field(is_optional=True)
