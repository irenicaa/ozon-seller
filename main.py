import os
import datetime

import dotenv

import credentials
import posting_fbo_list

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = posting_fbo_list.PaginatedGetPostingFBOListFilter(
        limit=2,
        offset=0,
        filter=posting_fbo_list.GetPostingFBOListFilter(
            since=datetime.datetime(2021, 11, 1),
            to=datetime.datetime(2023, 11, 1),
            status='awaiting_packaging',
        ),
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    for list in posting_fbo_list.get_posting_fbo_list_iterative(ozon_credentials, data):
        print(list)
