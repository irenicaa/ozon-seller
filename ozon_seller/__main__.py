import datetime
import os

import dotenv

from . import credentials, posting_fbs_list

if __name__ == "__main__":
    dotenv.load_dotenv()
    data = posting_fbs_list.PaginatedGetPostingFBSListFilter(
        limit=2,
        offset=0,
        filter=posting_fbs_list.GetPostingFBSListFilter(
            since=datetime.datetime(2021, 11, 1),
            to=datetime.datetime(2023, 11, 1),
            status='awaiting_packaging',
        ),
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    list = posting_fbs_list.get_posting_fbs_list(ozon_credentials, data)
    print(list)
