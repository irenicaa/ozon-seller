import os

import dotenv

import credentials
import posting_fbs_list

if __name__ == '__main__':
    dotenv.load_dotenv()
    data = posting_fbs_list.GetFbsPostingListRequest(
        limit=2,
        offset=0,
        filter=posting_fbs_list.GetFbsPostingListRequestFilter(
            since='2021-11-01T00:00:00.000Z',
            status='awaiting_packaging',
            to='2023-12-01T23:59:59.000Z',
        ),
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    list = posting_fbs_list.get_posting_fbs_list(ozon_credentials, data)
    print(list)
