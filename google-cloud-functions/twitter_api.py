
"""
# Requirements Text
tweepy==4.12.1
requests==2.28.1
pandas==1.5.2
gcsfs==2022.11.0"""


import tweepy
import os
import requests
import pandas as pd
#import gcsfs

os.getcwd()
print(os.getcwd())

def lookup_twitter_user():
#def lookup_twitter_user(client):
    client = tweepy.Client( bearer_token=os.environ.get('twitter_bearer_token'), 
                            consumer_key=os.environ.get('consumer_key'), 
                            consumer_secret=os.environ.get('consumer_secret'), 
                            access_token=os.environ.get('twitter_access_token'), 
                            access_token_secret=os.environ.get('twitter_access_token_secret'), 
                            return_type = requests.Response,
                            wait_on_rate_limit=True)
    
    # Define query
    query = 'from:POTUS -is:retweet'

    # get max. 100 tweets
    tweets = client.search_recent_tweets(query=query, 
                                        tweet_fields=['author_id', 'created_at'],
                                        max_results=10)


    # Save data as dictionary
    tweets_dict = tweets.json() 

    # Extract "data" value from dictionary
    tweets_data = tweets_dict['data'] 

    # Transform to pandas Dataframe
    df = pd.json_normalize(tweets_data) 
    print(df.head(10))

    return tweets_dict

lookup_twitter_user()
