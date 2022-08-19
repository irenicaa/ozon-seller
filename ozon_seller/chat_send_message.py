from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json

from .common import credentials, request_api

# Request


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class ChatMessageData:
    chat_id: Optional[str] = None
    text: Optional[str] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetChatStartResponseResult:
    result: str


def send_message(
    credentials: credentials.Credentials,
    data: ChatMessageData,
) -> GetChatStartResponseResult:
    return request_api.request_api_json(
        "POST",
        "/v1/chat/send/message",
        credentials,
        data,
        response_cls=GetChatStartResponseResult,
    )
