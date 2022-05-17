import json
import os

import requests
import dotenv

if __name__ == '__main__':
    dotenv.load_dotenv()

    session = requests.Session()
    response = session.post(
        'https://api-seller.ozon.ru/v3/product/info/stocks',
        headers={'Client-Id': os.getenv('OZON_CLIENT_ID'), 'Api-Key': os.getenv('OZON_API_KEY')},
        data=json.dumps({'limit': 100, 'last_id': '', 'filter': {'visibility': 'ALL'}}),
    )
    response.raise_for_status()

    stocks = response.json()
    print(stocks)
