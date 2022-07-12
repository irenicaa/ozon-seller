import json
from typing import Generic, Optional, TypeVar

import requests

from . import credentials, error_response

T = TypeVar("T")


class HTTPError(RuntimeError, Generic[T]):
    def __init__(
        self,
        message: str,
        status: int,
        response_data: T,
        *args,
    ):
        super().__init__(message, status, response_data, *args)

        self.message = message
        self.status = status
        self.response_data = response_data


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
        raise HTTPError(response.text, response.status_code, response.text)

    return response


def request_api_json(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[object],
    *,
    response_cls: type[T],
    error_cls: object = error_response.ErrorResponse,
) -> T:
    try:
        response = request_api_raw(
            method,
            endpoint,
            credentials,
            data.to_json() if data is not None else None,
        )
        return response_cls.schema().loads(response.text)
    except HTTPError as error:
        response_data = error_cls.schema().loads(error.response_data)
        raise HTTPError(error.message, error.status, response_data)
