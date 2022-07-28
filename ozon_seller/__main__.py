import datetime
import os

import dotenv

from . import chat_start, credentials, request_api, stocks

if __name__ == "__main__":
    dotenv.load_dotenv()
    try:
        data = chat_start.ChatStartData(
            posting_number=os.getenv('POSTING_NUMBER')
        )
        print(data.to_json())

        ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))

        chat_id = chat_start.get_product_info_stocks(ozon_credentials, data)
        print(chat_id)

    except request_api.HTTPError as error:
        print('ERROR', error)
        print('ERROR response_data', error.response_data)
