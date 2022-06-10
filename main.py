import os
import datetime

import dotenv

import credentials
import posting_fbs_ship

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = posting_fbs_ship.PostingFBSShip(
        posting_number='',
        packages=[posting_fbs_ship.PostingShipRequestPackages(
            items=posting_fbs_ship.FBSPackageItem(
                mandatory_mark=['string'],
                quantity=1,
                sku=00000,
            )
        )]

    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    posting_fbs_ship.posting_fbs_ship(ozon_credentials, data)
    print(list)
