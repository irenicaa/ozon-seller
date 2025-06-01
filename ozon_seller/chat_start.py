from dataclasses import dataclass
from typing import Optional

from .common import credentials, request_api
from .common.data_class_json_mixin import DataClassJsonMixin


# Request


@dataclass
class ChatStartData(DataClassJsonMixin):
    posting_number: Optional[str] = None


# Response


@dataclass
class GetChatStartResponseResult(DataClassJsonMixin):
    chat_id: str


@dataclass
class GetChatStartResponseResultWrapper(DataClassJsonMixin):
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
