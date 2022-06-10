import os
import datetime

import dotenv

import credentials
import posting_fbs_ship_gtd

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = posting_fbs_ship_gtd.PostingFBSShip(
        posting_number='',
        packages=[posting_fbs_ship_gtd.PostingShipRequestPackages(
            products=[posting_fbs_ship_gtd.FBSPackageProducts(
                quantity=1,
                product_id=000000,
                exemplar_info=[posting_fbs_ship_gtd.FBSProductExemplarInfo(
                gtd='string',
                 )]
            )],
        )]

    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    posting_fbs_ship_gtd.posting_fbs_ship(ozon_credentials, data)
    print(list)
