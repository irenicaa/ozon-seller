import datetime
import os

import dotenv

from . import char_send_message, credentials, request_api, stocks

if __name__ == "__main__":
    dotenv.load_dotenv()
    try:
        data = char_send_message.ChatMessageData(
            chat_id=os.getenv('CHAT_ID'),
            text="Hello World!"
        )
        print(data.to_json())

        ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))

        result = char_send_message.send_message(ozon_credentials, data)
        print(result)

    except request_api.HTTPError as error:
        print('ERROR', error)
        print('ERROR response_data', error.response_data)
