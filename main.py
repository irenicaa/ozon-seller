import json
import os

import requests
import dotenv

import request_api
import credentials
import stocks

if __name__ == '__main__':
    dotenv.load_dotenv()

    filter = stocks.PaginatedProductFilter(
        filter=stocks.ProductFilter(
            offer_id=['1', '2', '3'],
            product_id=['4', '5', '6'],
            visibility='ALL',
        ),
        limit=100,
        last_id='',
    )
    print(filter.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    data = {'limit': 100, 'last_id': '', 'filter': {'visibility': 'ALL'}}
    stocks = request_api.request_api('POST', '/v3/product/info/stocks', ozon_credentials, data)
    print(stocks)
