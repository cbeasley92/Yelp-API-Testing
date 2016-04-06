import io
import json
import requests

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# Author:       Clinton Beasley
# Date:         April 6, 2016
# Title:        yelp_api.py
# Description:  Testing integration with the Yelp API

# read API keys from config file
with io.open('config.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)


def get_search_dallas():
    params = {
        'term': 'food',
        'lang': 'en'
    }

    response = client.search('Dallas', **params)

    print type(response)


def main():
    print 'Searching Yelp for Dallas'
    get_search_dallas()

main()
