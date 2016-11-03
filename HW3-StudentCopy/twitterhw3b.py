# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob
import re

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

public_tweets = api.search('"Gilmore Girls" @netflix')

total_polarity = 0.0
total_subjectivity = 0.0
count = 0
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	
	sub_and_pol = str(analysis.sentiment)

	tweet_sentiment_polarity = re.findall('polarity=\-?[\d].[\d]+', sub_and_pol)
	string, polarity = tweet_sentiment_polarity[0].split('=')

	tweet_sentiment_subjectivity = re.findall('subjectivity=\-?[\d].[\d]+', sub_and_pol)
	string, subjectivity = tweet_sentiment_subjectivity[0].split('=')
	
	count += 1
	total_polarity += float(polarity)
	total_subjectivity += float(subjectivity)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data


print("Average subjectivity is "+str(total_subjectivity/count))
print("Average polarity is "+str(total_polarity/count))
