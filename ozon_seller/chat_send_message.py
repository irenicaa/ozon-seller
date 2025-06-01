from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ChatMessageData(DataClassJsonMixin):
    chat_id: Optional[str] = None
    text: Optional[str] = None


# Response


@dataclass
class GetChatStartResponseResult(DataClassJsonMixin):
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
