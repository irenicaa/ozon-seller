import os

import dotenv

import credentials
import product_description

if __name__ == '__main__':
    dotenv.load_dotenv()
    data = product_description.ProductData(offer_id='0008')
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    list =  product_description.get_product_description(ozon_credentials, data)
    print(list)
