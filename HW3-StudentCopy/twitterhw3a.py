# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
OAUTH_TOKEN = "726175519004205056-FafWgRYKWqcmW8aO7uhmrk8g2dEls3E"
OAUTH_TOKEN_SECRET = "sLkovs0k8i58V7pfFCxM9k2m511BQwSdAdA8M6qNsuxGu"
APP_KEY = "ykGXCbMxJqqMZWY3Ca5LKtawS"
APP_SECRET = "83DgYkMS3IPsfnyqpBVOjCBzzcHUIv3tARnP7kWLjzZLz0bm9o"


from twython import Twython
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('/Users/AditiRajadhyaksha/Desktop/project3/HW3-StudentCopy/media/tweet_image.jpg', 'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status='Submission for SI 206 Project 3 #UMSI-206 #Proj3', media_ids=[response['media_id']])