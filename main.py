import os

import dotenv

import credentials
import actions

if __name__ == '__main__':
    dotenv.load_dotenv()

    ozon_credentials = credentials.Credentials(os.getenv('OZON_CLIENT_ID'), os.getenv('OZON_API_KEY'))
    actions = actions.get_actions(ozon_credentials, '')
    print(actions)
