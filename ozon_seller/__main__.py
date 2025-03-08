import datetime
import os

import dotenv

from . import product_info_attributes
from .common import credentials, http_error

if __name__ == "__main__":
    dotenv.load_dotenv()
    try:
        data = product_info_attributes.PaginatedProductFilter(
            filter=product_info_attributes.ProductFilter(
                offer_id=[],
                product_id=[],
                sku=[""],
                visibility="ALL",
            ),
            limit=1,
            last_id="",
            sort_dir="ASC",
        )
        print(data.to_json())

        ozon_credentials = credentials.Credentials(
            os.getenv("OZON_CLIENT_ID"), os.getenv("OZON_API_KEY")
        )
        status = product_info_attributes.get_product_attributes(
            ozon_credentials, data
        )
        print(status)
    except http_error.HTTPError as error:
        print("ERROR", error)
        print("ERROR response_data", error.response_data)
