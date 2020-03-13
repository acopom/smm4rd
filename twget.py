import tweepy
import time

consumer_key = "key"
consumer_secret = "key secret"
access_token = "token"
access_token_secret = "token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.user_timeline, id="userid").items():
  time.sleep(1)
  if (list(tweet.text)[:2]!=['R', 'T']) & (list(tweet.text)[0]!='@'):
    print(tweet.created_at, end="\t")
    print(tweet.text)
