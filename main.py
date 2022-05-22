import json
import os

import requests
import dotenv

import request_api
import credentials
import stocks

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = stocks.PaginatedProductFilter(
        filter=stocks.ProductFilter(
            offer_id=[],
            product_id=[],
            visibility='ALL',
        ),
        limit=10,
        last_id='',
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    stocks = stocks.get_product_info_stocks(ozon_credentials, data)
    print(stocks)
