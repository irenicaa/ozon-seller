import datetime
import os

import dotenv

from . import product_pictures_import
from .common import credentials, http_error

if __name__ == "__main__":
    dotenv.load_dotenv()
    try:
        data = product_pictures_import.ProductPictures(
            images=[
                "https://disk.yandex.ru/i/MD7epp4HEH8kyg",
            ],
            product_id=870343542,
        )
        print(data.to_json())

        ozon_credentials = credentials.Credentials(
            os.getenv("OZON_CLIENT_ID"), os.getenv("OZON_API_KEY")
        )

        stocks = product_pictures_import.send_product_pictures(ozon_credentials, data)
        print(stocks)
    except http_error.HTTPError as error:
        print("ERROR", error)
        print("ERROR response_data", error.response_data)
