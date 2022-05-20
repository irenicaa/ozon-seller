import json
import os

import requests
import dotenv

import request_api
import credentials

if __name__ == '__main__':
    dotenv.load_dotenv()

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    data = {'limit': 100, 'last_id': '', 'filter': {'visibility': 'ALL'}}
    stocks = request_api.request_api('POST', '/v3/product/info/stocks', ozon_credentials, data)
    print(stocks)
