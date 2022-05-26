import json

import requests

import credentials

def request_api_raw(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: str,
) -> str:
    session = requests.Session()
    response = session.request(
        method,
        'https://api-seller.ozon.ru' + endpoint,
        headers=credentials.to_headers(),
        data=data,
    )
    print(response.text)
    response.raise_for_status()

    return response.text

def request_api(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: object,
) -> object:
    json_data = json.dumps(data)
    response = request_api_raw(method, endpoint, credentials, json_data)
    return json.loads(response)
