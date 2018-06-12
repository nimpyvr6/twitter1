
import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'hEPhQr3n56kIHyS8aVzuk6KtY'
CONSUMER_SECRET = 'p5m1VuRfEhfSCWMnu0eaXVb2DpWlXh8JM4AfXVFOegKXQ85t6W'
OAUTH_TOKEN = '259861500-7zfkibFIVnoFaE6Uu6BgncB2GNDpOG6UJmTtfH2J'
OAUTH_TOKEN_SECRET = 'iSowbAAnZA5GrLEOtjpWH0cWCgkymNHffJNUsYdwxQA3r'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print(json.dumps(dub_trends, indent=1))
