import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import (
    CatchAll,
    Undefined,
    config,
    dataclass_json,
    DataClassJsonMixin,
)
from marshmallow import fields

from .common import credentials, request_api

# Request


@dataclass
class FBSPackageData(DataClassJsonMixin):
    posting_number: list[str]


def get_posting_fbs_package_label(
    credentials: credentials.Credentials,
    data: FBSPackageData,
) -> bytes:
    response = request_api.request_api_raw(
        "POST",
        "/v2/posting/fbs/package-label",
        credentials,
        data.to_json(),
    )
    return response.content
