import datetime
from dataclasses import dataclass, field
from typing import Generator, Optional

from dataclasses_json import CatchAll, Undefined, config, dataclass_json
from marshmallow import fields

import credentials
import request_api

# Request


@dataclass_json
@dataclass
class FBSPackageData:
    posting_number: list[str]


# Response


@dataclass_json
@dataclass
class PostingFBSResonseResult:
    content: bytes


def get_posting_fbs_package_label(
    credentials: credentials.Credentials,
    data: FBSPackageData,
) -> bytes:
    response = request_api.request_api_content(
        "POST",
        "/v2/posting/fbs/package-label",
        credentials,
        data.to_json(),
    )
    return response
