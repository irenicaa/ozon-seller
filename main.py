import json
import os
import time
import datetime

import requests
import dotenv

import request_api
import credentials
import stocks
import returns_fbs
import product_info


if __name__ == '__main__':
    dotenv.load_dotenv()

    data = product_info.ProductData(
        offer_id='0008'
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    product = product_info.get_product_info(ozon_credentials, data)
    print(product)
