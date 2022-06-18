import os
import datetime

import dotenv

import credentials
import posting_fbs_package_label

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = posting_fbs_package_label.FBSPackageData(
        posting_number=[os.getenv('OZON_ORDER_ID')])
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    pdf = posting_fbs_package_label.get_posting_fbs_package_label(ozon_credentials, data)
    with open('test.pdf', 'wb') as f:
        f.write(pdf)
