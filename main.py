import os
import datetime

import dotenv

import credentials
import posting_fbs_get

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = posting_fbs_get.PostingFBSData(posting_number='')
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    list = posting_fbs_get.get_posting_fbs_data(ozon_credentials, data)
    print(list)
