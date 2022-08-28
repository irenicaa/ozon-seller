import datetime
import os

import dotenv

from . import products_stocks, stocks
from .common import credentials, http_error

if __name__ == "__main__":
    dotenv.load_dotenv()
    try:
        data = products_stocks.StocksData(
            stocks=[products_stocks.ProductData(
                offer_id="00001",
                stock=26,
                warehouse_id=22182581590000,
            )],
        )
        print(data.to_json())

        ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
        status = products_stocks.set_stocks(ozon_credentials, data)
        print(status)
    except http_error.HTTPError as error:
        print('ERROR', error)
        print('ERROR response_data', error.response_data)
