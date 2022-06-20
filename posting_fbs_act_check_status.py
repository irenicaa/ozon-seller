from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json
from marshmallow import fields

import request_api
import credentials



# Request

@dataclass_json
@dataclass
class PostingFSBActData:
    id: Optional[int] = None

# Response

@dataclass_json
@dataclass
class PostingFBSActCheckStatusResponseResult:
    act_type: str
    added_to_act: list[str]
    removed_from_act: list[str]
    status: str

@dataclass_json
@dataclass
class PostingFBSActCreateResponseActResultWrapper:
    result: PostingFBSActCheckStatusResponseResult

def create_posting_fbs_act(
    credentials: credentials.Credentials,
    data: PostingFSBActData,
) -> PostingFBSActCreateResponseActResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v2/posting/fbs/act/check-status',
        credentials,
        data.to_json(),
    )
    return PostingFBSActCreateResponseActResultWrapper.schema().loads(response)
