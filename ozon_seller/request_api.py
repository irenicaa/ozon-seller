import json
from typing import Optional, Type, TypeVar

import requests

from . import credentials


class HTTPError(RuntimeError):
    def __init__(self, message, status, *args):
        super().__init__(message, status, *args)

        self.status = status


T = TypeVar("T")


def request_api_raw(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[str],
) -> requests.models.Response:
    session = requests.Session()
    response = session.request(
        method,
        "https://api-seller.ozon.ru" + endpoint,
        headers=credentials.to_headers(),
        data=data,
    )
    if response.status_code < 200 or response.status_code >= 300:
        raise HTTPError(response.text, response.status_code)

    return response


def request_api_json(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[object],
    *,
    response_cls: Type[T],
) -> T:
    response = request_api_raw(
        method,
        endpoint,
        credentials,
        data.to_json() if data is not None else None,
    )
    return response_cls.schema().loads(response.text)
