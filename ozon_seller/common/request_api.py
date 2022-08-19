from typing import Optional, TypeVar

import requests

from . import credentials, error_response, http_error

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
        # use the response text both as an error message and as an error response data
        raise http_error.HTTPError(response.text, response.status_code, response.text)

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
    except http_error.HTTPError as error:
        response_data = error_cls.schema().loads(error.response_data)
        raise http_error.HTTPError(error.message, error.status, response_data)
