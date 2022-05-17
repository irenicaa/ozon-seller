import json
import os

import requests
import dotenv

import request_api

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = {'limit': 100, 'last_id': '', 'filter': {'visibility': 'ALL'}}
    stocks = request_api.request_api('/v3/product/info/stocks', os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'), data)
    print(stocks)
