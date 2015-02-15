#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'XXXXXXXXXXXX'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'XXXXXXXXXXXX'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'XXXXXXxXXXXXXXXXXXXXXX'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXX'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status=line)
    seed = random.randrange(1,6)# Post status at random interval
    print seed
    time.sleep(seed*100)#convert time in minutes
