import os

import dotenv

import credentials
import actions_products

if __name__ == '__main__':
    dotenv.load_dotenv()
    data = actions_products.PaginatedActionProducts(
        action_id = 384251,
        limit=2,
        offset=0,
    )
    print(data.to_json())

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    for product in actions_products.get_action_products_iterative(ozon_credentials, data):
        print(product)
