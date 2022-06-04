import os
import datetime

import dotenv

import credentials
import posting_fbs_product_country_list

if __name__ == '__main__':
    dotenv.load_dotenv()

    data = posting_fbs_product_country_list.CountryFilter()
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    list = posting_fbs_product_country_list.get_fbs_product_country_list(ozon_credentials, data)
    print(list)
