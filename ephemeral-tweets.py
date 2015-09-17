#!/usr/bin/env python
# ephemeral tweets // @x42___
# requirement: pip install python-twitter
# usage: python ephemeral-tweets.py &

import twitter
import time
import random

# secrets, keys and tokens. create an app at apps.twitter.com to get some
api = twitter.Api(consumer_key='',
                consumer_secret='',
                access_token_key='',
                access_token_secret='')

while True:
    handle = 'x42___' # your username
    statuses = api.GetUserTimeline(str(handle), since_id = 0, count = 1)
    for status in statuses:
        time.sleep(3600 * random.random())
        api.DestroyStatus(status.id)
        break
