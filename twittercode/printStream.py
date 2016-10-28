import tweepy
import json

# Unique code from Twitter
access_token = "726175519004205056-FafWgRYKWqcmW8aO7uhmrk8g2dEls3E"
access_token_secret = "sLkovs0k8i58V7pfFCxM9k2m511BQwSdAdA8M6qNsuxGu"
consumer_key = "ykGXCbMxJqqMZWY3Ca5LKtawS"
consumer_secret = "83DgYkMS3IPsfnyqpBVOjCBzzcHUIv3tARnP7kWLjzZLz0bm9o"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


