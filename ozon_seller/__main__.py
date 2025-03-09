import datetime
import os

import dotenv

from . import stocks
from .common import credentials, http_error

if __name__ == "__main__":
    dotenv.load_dotenv()
    try:
        data = stocks.PaginatedProductFilter(
            cursor="",
            filter=stocks.ProductFilter(
                visibility="ALL",
            ),
            limit=100,
        )
        print(data.to_json())

        ozon_credentials = credentials.Credentials(
            os.getenv("OZON_CLIENT_ID"), os.getenv("OZON_API_KEY")
        )
        stocks = stocks.get_product_info_stocks_iterative(
            ozon_credentials, data
        )
        for stock in stocks:
            print(stock)
    except http_error.HTTPError as error:
        print("ERROR", error)
        print("ERROR response_data", error.response_data)
