import io
import json
import time
import logging

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# Author:       Clinton Beasley
# Date:         April 6, 2016
# Title:        yelp_api.py
# Description:  Testing integration with the Yelp API

# Configure Logging
formatting = '%(asctime)-15s %(message)s'
logging.Formatter.converter = time.gmtime
logging.basicConfig(filename=r'yelp_testing.log', format=formatting, level=logging.INFO)

# read API keys from config file
with io.open('config.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)
    logging.info('Client Authorized')


def get_search_dallas():
    params = {
        'term': 'food',
        'lang': 'en'
    }

    logging.info('Searching Yelp in Dallas')
    logging.info('Passing parameters: %s' % str(params))

    response = client.search('Dallas', **params)

    # print type(response)
    # print response.businesses

    print '%-*s%s' % (35, 'Name', 'Rating')
    logging.info('%-*s%s' % (35, 'Name', 'Rating'))

    for x in response.businesses:
        print '%-*s%s' % (35, x.name, x.rating)
        logging.info('%-*s%s' % (35, x.name, x.rating))


def main():
    print 'Searching Yelp for Dallas'
    get_search_dallas()

main()
