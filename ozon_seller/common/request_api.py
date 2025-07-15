from typing import Optional, TypeVar, cast

import requests

from . import credentials, error_response, http_error
from .data_class_json_mixin import DataClassJsonMixin


T = TypeVar("T", bound=DataClassJsonMixin)


_API_BASE_URL = "https://api-seller.ozon.ru"


def request_api_raw(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[str],
) -> requests.models.Response:
    if not endpoint.startswith("/"):
        raise ValueError("the endpoint should start with a slash")

    session = requests.Session()
    response = session.request(
        method,
        _API_BASE_URL + endpoint,
        headers=credentials.to_headers(),
        data=data,
    )
    if response.status_code < 200 or response.status_code >= 300:
        # use the response text both as an error message
        # and as an error response data
        raise http_error.HTTPError(
            response.text,
            response.status_code,
            response.text,
        )

    return response


def request_api_content(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[DataClassJsonMixin],
    *,
    error_cls: type[DataClassJsonMixin] = error_response.ErrorResponse,
) -> bytes:
    try:
        raw_data = data.to_json() if data is not None else None
        response = request_api_raw(method, endpoint, credentials, raw_data)
        return response.content
    except http_error.HTTPError as error:
        response_data = error_cls.schema().loads(error.response_data)
        raise http_error.HTTPError(error.message, error.status, response_data) from None


def request_api_json(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[DataClassJsonMixin],
    *,
    response_cls: type[T],
    error_cls: type[DataClassJsonMixin] = error_response.ErrorResponse,
) -> T:
    content = request_api_content(method, endpoint, credentials, data, error_cls=error_cls)
    return cast(T, response_cls.schema().loads(content))
