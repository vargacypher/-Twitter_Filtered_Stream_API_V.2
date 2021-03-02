# -*- coding: utf-8 -*-
__author__ = 'Guilherme Cardoso de Vargas'
__version__ = 1.0
__maintainer__ = 'Guilherme Cardoso de Vargas'
__email__ = 'vargas93626@gmail.com'
__status__ = 'Prototype'

from datetime import datetime
from TwitterSearch import *
import json

access_token = '<your_token>'
access_token_secret = '<your_token>'
consumer_key = '<your_token>'
consumer_secret = '<your_token>'

try:

    ts = TwitterSearch(
        access_token = access_token,
        access_token_secret = access_token_secret,
        consumer_key = consumer_key,
        consumer_secret = consumer_secret
    )
    
    tso = TwitterSearchOrder()
    tso.set_keywords(['covid','saúde'])
    tso.set_language('pt')
    

    for tweet in ts.search_tweets_iterable(tso):
        print('created_at:',tweet['created_at'],'ID:',tweet['id_str'],'Tweet:',tweet['text'])

        created_at = tweet['created_at']
        ID = tweet['id_str']
        texto = tweet['text']

        with open('tweet.json','a+') as output:

            data = { "created_at":created_at,
            "ID":ID,
            "tweet":texto}
            print(data)
            output.write("{}\n".format(json.dumps(data)))

except TwitterSearchException as e:
    print(e)
