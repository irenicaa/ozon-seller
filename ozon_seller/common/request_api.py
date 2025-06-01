from typing import Optional, TypeVar, cast

import requests

from . import credentials, error_response, http_error
from .data_class_json_mixin import DataClassJsonMixin


T = TypeVar("T", bound=DataClassJsonMixin)


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
        # use the response text both as an error message
        # and as an error response data
        raise http_error.HTTPError(
            response.text,
            response.status_code,
            response.text,
        )

    return response


def request_api_json(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[DataClassJsonMixin],
    *,
    response_cls: type[T],
    error_cls: type[DataClassJsonMixin] = error_response.ErrorResponse,
) -> T:
    try:
        response = request_api_raw(
            method,
            endpoint,
            credentials,
            data.to_json() if data is not None else None,
        )
        return cast(T, response_cls.schema().loads(response.text))
    except http_error.HTTPError[str] as error:
        response_data = error_cls.schema().loads(error.response_data)
        raise http_error.HTTPError(error.message, error.status, response_data)
