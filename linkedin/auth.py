import requests
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = 'https://www.linkedin.com/oauth/v2/accessToken'

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']


def get_access_token():
    response = requests.get(endpoint, params={
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret})

    print(response.json())


get_access_token()
