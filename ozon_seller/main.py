import datetime
import os

import dotenv

from . import credentials, posting_fbs_ship_gtd

if __name__ == "__main__":
    dotenv.load_dotenv()
    date = datetime.datetime(2022, 6, 20)
    time = datetime.time(16, 34)
    data = posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
        posting_number='49142079-0101-2',
        packages=[posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
            products=[posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                quantity=1,
                product_id='322467929',
                exemplar_info=[posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                gtd='string',
                 )]
            )],
        )]
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(
        os.getenv("OZON_CLIENT_ID"), os.getenv("OZON_API_KEY")
    )
    status = posting_fbs_ship_gtd.create_posting_fbs_ship_with_gtd(ozon_credentials, data)
    print(status)
