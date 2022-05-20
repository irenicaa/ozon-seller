import json

import requests

import credentials

def request_api(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: object,
) -> object:
    session = requests.Session()
    response = session.request(
        method,
        'https://api-seller.ozon.ru' + endpoint,
        headers=credentials.to_headers(),
        data=json.dumps(data),
    )
    response.raise_for_status()

    return response.json()
