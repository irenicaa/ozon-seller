import datetime
import os

import dotenv

from . import credentials, posting_fbs_act_check_status

if __name__ == "__main__":
    dotenv.load_dotenv()
    date = datetime.datetime(2022, 6, 20)
    time = datetime.time(16, 34)
    data = posting_fbs_act_check_status.PostingFSBActData(
        id=int(os.getenv("OZON_ACT_ID")),
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(
        os.getenv("OZON_CLIENT_ID"), os.getenv("OZON_API_KEY")
    )
    status = posting_fbs_act_check_status.create_posting_fbs_act(ozon_credentials, data)
    print(status)
