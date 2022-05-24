import json
import os
import time
import datetime

import requests
import dotenv
from typing import Optional

import request_api
import credentials
import stocks
import returns_fbs

if __name__ == '__main__':
    dotenv.load_dotenv()
    data = returns_fbs.ProductFilter(
        filter=returns_fbs.returnsGetReturnsCompanyFBSRequestFilter(
        accepted_from_customer_moment=returns_fbs.FilterTimeRange(
            time_from=datetime.datetime(2022, 5, 1),
            time_to = datetime.datetime(2022, 5, 24),
        ),
        last_free_waiting_day=None,
        posting_number=None,
        ),
        limit=10,
        offset=0,
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    for returned in returns_fbs.get_returns_from_fbs_iterative(ozon_credentials, data):
        print(returned)
        time.sleep(2)
