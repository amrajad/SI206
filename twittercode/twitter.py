import tweepy

# Unique code from Twitter
access_token = "726175519004205056-FafWgRYKWqcmW8aO7uhmrk8g2dEls3E"
access_token_secret = "sLkovs0k8i58V7pfFCxM9k2m511BQwSdAdA8M6qNsuxGu"
consumer_key = "ykGXCbMxJqqMZWY3Ca5LKtawS"
consumer_secret = "83DgYkMS3IPsfnyqpBVOjCBzzcHUIv3tARnP7kWLjzZLz0bm9o"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


for tweet in public_tweets:
	print(tweet.text)
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

