import sys
import os
import os.path
import logging

# requires: python3 -m pip install "python-dotenv >= 0.7.1, < 1.0.0"
import dotenv

# add the project root directory to `sys.path` so that the `ozon_seller` package
# can be imported without installing it (this is useful during development)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ozon_seller.common import credentials, http_error
from ozon_seller import stocks


def _run_request(credentials: credentials.Credentials, logger: logging.Logger) -> None:
    data = stocks.PaginatedProductFilter(
        filter=stocks.ProductFilter(
            visibility="VISIBLE",
        ),
        cursor="",
        limit=1000,
    )
    logger.info("request payload: %s", data.to_json())

    for item in stocks.get_product_info_stocks_iterative(credentials, data):
        logger.info("stock item: %r", item)


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
    dotenv.load_dotenv()

    logger = logging.getLogger(__name__)
    try:
        request_credentials = credentials.Credentials(
            os.getenv("OZON_CLIENT_ID", ""),
            os.getenv("OZON_API_KEY", ""),
        )

        _run_request(request_credentials, logger)
    except http_error.HTTPError as error:
        logger.error("HTTP error occurred: status = %d; message = %r", error.status, error.message)
        logger.error("HTTP error occurred: response data = %r", error.response_data)
