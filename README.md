# ozon-seller

[![lint](https://github.com/irenicaa/ozon-seller/actions/workflows/lint.yaml/badge.svg)](https://github.com/irenicaa/ozon-seller/actions/workflows/lint.yaml)
[![test](https://github.com/irenicaa/ozon-seller/actions/workflows/test.yaml/badge.svg)](https://github.com/irenicaa/ozon-seller/actions/workflows/test.yaml)

A library that implements a client for [Ozon Seller API](https://docs.ozon.ru/api/seller/en/).

## Features

- common features:
  - use [dataclasses](https://docs.python.org/3/library/dataclasses.html) for all the request and responses
  - support for automatic JSON serialization and parsing for all the request and responses, respectively
  - implement iterators for the endpoints with pagination
  - powerful error handling — for each error is available:
    - HTTP status
    - [Ozon Seller API](https://docs.ozon.ru/api/seller/en/) error code and message
- implemented endpoints:
  - [**Uploading and updating products:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/ProductAPI)
    - [Upload and update product images](https://docs.ozon.ru/api/seller/en/#operation/ProductAPI_ProductImportPictures):
      - endpoint: `POST /v1/product/pictures/import`
      - module: [ozon_seller.product_pictures_import](ozon_seller/product_pictures_import.py)
    - [Get a description of the product characteristics](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ProductAPI_GetProductAttributesV4):
      - endpoint: `POST /v4/product/info/attributes`
      - module: [ozon_seller.product_info_attributes](ozon_seller/product_info_attributes.py)
    - [Get product description](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ProductAPI_GetProductInfoDescription):
      - endpoint: `POST /v1/product/info/description`
      - module: [ozon_seller.product_description](ozon_seller/product_description.py)
  - [**Prices and Stocks:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/PricesandStocksAPI)
    - [Update the quantity of products in stock](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ProductAPI_ProductsStocksV2):
      - endpoint: `POST /v2/products/stocks`
      - modules:
        - [ozon_seller.product_import_stocks](ozon_seller/product_import_stocks.py)
        - [ozon_seller.products_stocks](ozon_seller/products_stocks.py)
    - [Information about product quantity](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ProductAPI_GetProductInfoStocks):
      - endpoint: `POST /v4/product/info/stocks`
      - module: [ozon_seller.stocks](ozon_seller/stocks.py)
    - [Update prices](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ProductAPI_ImportProductsPrices):
      - endpoint: `POST /v1/product/import/prices`
      - module: [ozon_seller.product_import_prices](ozon_seller/product_import_prices.py)
  - [**Promotions:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/Promos)
    - [Available promotions](https://docs.ozon.ru/api/seller/en/#tag/Promos/paths/~1v1~1actions/get):
      - endpoint: `GET /v1/actions`
      - module: [ozon_seller.actions](ozon_seller/actions.py)
    - [Products that can participate in a promotion](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PromosCandidates):
      - endpoint: `POST /v1/actions/candidates`
      - module: [ozon_seller.actions_candidates](ozon_seller/actions_candidates.py)
    - [Products in a promotion](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PromosProducts):
      - endpoint: `POST /v1/actions/products`
      - module: [ozon_seller.actions_products](ozon_seller/actions_products.py)
  - [**FBS and rFBS orders processing:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/FBS)
    - [Shipments list (version 3)](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_GetFbsPostingListV3):
      - endpoint: `POST /v3/posting/fbs/list`
      - module: [ozon_seller.posting_fbs_list](ozon_seller/posting_fbs_list.py)
    - [Get shipment details by identifier (version 3)](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_GetFbsPostingV3):
      - endpoint: `POST /v3/posting/fbs/get`
      - module: [ozon_seller.posting_fbs_get](ozon_seller/posting_fbs_get.py)
    - [List of manufacturing countries](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_ListCountryProductFbsPostingV2):
      - endpoint: `POST /v2/posting/fbs/product/country/list`
      - module: [ozon_seller.posting_fbs_product_country_list](ozon_seller/posting_fbs_product_country_list.py)
    - [Set the manufacturing country](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_SetCountryProductFbsPostingV2):
      - endpoint: `POST /v2/posting/fbs/product/country/set`
      - module: [ozon_seller.posting_fbs_product_country_set](ozon_seller/posting_fbs_product_country_set.py)
    - [Print the labeling](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_PostingFBSPackageLabel):
      - endpoint: `POST /v2/posting/fbs/package-label`
      - module: [ozon_seller.posting_fbs_package_label](ozon_seller/posting_fbs_package_label.py)
  - [**FBO:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/FBO)
    - [Shipments list](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_GetFboPostingList):
      - endpoint: `POST /v2/posting/fbo/list`
      - module: [ozon_seller.posting_fbo_list](ozon_seller/posting_fbo_list.py)
  - [**FBS delivery:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/DeliveryFBS)
    - [Create an acceptance and transfer certificate and a waybill](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_PostingFBSActCreate):
      - endpoint: `POST /v2/posting/fbs/act/create`
      - module: [ozon_seller.posting_fbs_act_create](ozon_seller/posting_fbs_act_create.py)
    - [List of shipments in the certificate](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_ActPostingList):
      - endpoint: `POST /v2/posting/fbs/act/get-postings`
      - module: [ozon_seller.fbs_act_get_postings](ozon_seller/fbs_act_get_postings.py)
    - [Barcode for product shipment](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_PostingFBSGetBarcode):
      - endpoint: `POST /v2/posting/fbs/act/get-barcode`
      - module: [ozon_seller.posting_fbs_act_get_barcode](ozon_seller/posting_fbs_act_get_barcode.py)
    - [Status of acceptance and transfer certificate and waybill](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/PostingAPI_PostingFBSActCheckStatus):
      - endpoint: `POST /v2/posting/fbs/act/check-status`
      - module: [ozon_seller.posting_fbs_act_check_status](ozon_seller/posting_fbs_act_check_status.py)
  - [**Chats with customers:**](https://docs.ozon.ru/api/seller/en/?__rr=1#tag/ChatAPI)
    - [Send message](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ChatAPI_ChatSendMessage):
      - endpoint: `POST /v1/chat/send/message`
      - module: [ozon_seller.chat_send_message](ozon_seller/chat_send_message.py)
    - [Create a new chat](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ChatAPI_ChatStart):
      - endpoint: `POST /v1/chat/start`
      - module: [ozon_seller.chat_start](ozon_seller/chat_start.py)
  - **outdated endpoints:**
    - ???:
      - endpoint: `POST /v2/product/info`
      - module: [ozon_seller.product_info](ozon_seller/product_info.py)
    - ???:
      - endpoint: `POST /v2/returns/company/fbo`
      - module: [ozon_seller.returns_fbo](ozon_seller/returns_fbo.py)
    - ???:
      - endpoint: `POST /v2/returns/company/fbs`
      - module: [ozon_seller.returns_fbs](ozon_seller/returns_fbs.py)
    - ???:
      - endpoint: `POST /v3/posting/fbs/ship`
      - module: [ozon_seller.posting_fbs_ship_gtd](ozon_seller/posting_fbs_ship_gtd.py)

## Installation

### From [PyPI](https://pypi.org/)

Install the library from [PyPI](https://pypi.org/):

```
$ python3 -m pip install ozon-seller
```

### From source

Clone this repository:

```
$ git clone https://github.com/irenicaa/ozon-seller
$ cd ozon-seller
```

Then install the library:

```
$ make install
```

## Examples

[Information about product quantity](https://docs.ozon.ru/api/seller/en/?__rr=1#operation/ProductAPI_GetProductInfoStocks):

```python
import sys
import os
import os.path
import logging

# requires: python3 -m pip install "python-dotenv >= 0.7.1, < 1.0.0"
import dotenv

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
```

## License

The MIT License (MIT)

Copyright &copy; 2025 irenica
