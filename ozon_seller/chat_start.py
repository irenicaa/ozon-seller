from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json

from . import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ChatStartData:
    posting_number: Optional[str] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetChatStartResponseResult:
    chat_id: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetChatStartResponseResultWrapper:
    result: GetChatStartResponseResult


def get_chat_id(
    credentials: credentials.Credentials,
    data: ChatStartData,
) -> GetChatStartResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v1/chat/start",
        credentials,
        data,
        response_cls=GetChatStartResponseResultWrapper,
    )
