import json
from typing import Optional

import requests

from . import credentials


class HTTPError(RuntimeError):
    def __init__(self, message, status, *args):
        super().__init__(message, status, *args)

        self.status = status


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
