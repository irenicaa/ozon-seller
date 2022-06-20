import os
import datetime

import dotenv

import credentials
import posting_fbs_act_create

if __name__ == '__main__':
    dotenv.load_dotenv()
    date = datetime.datetime(2022, 6, 20)
    time = datetime.time(16, 34)
    data = posting_fbs_act_create.PostingFSBDeliveryData(
        delivery_method_id=int(os.getenv('OZON_DELIVERY_METHOD_ID')),
        departure_date=datetime.datetime.combine(date.date(), time)
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    pdf = posting_fbs_act_create.create_posting_fbs_act(ozon_credentials, data)
