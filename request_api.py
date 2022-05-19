import json

import requests

def request_api(
    endpoint: str,
    client_id: str,
    api_key: str,
    data: object,
) -> object:
    session = requests.Session()
    response = session.post(
        'https://api-seller.ozon.ru' + endpoint,
        headers={'Client-Id': client_id, 'Api-Key': api_key},
        data=json.dumps(data),
    )
    response.raise_for_status()

    return response.json()
