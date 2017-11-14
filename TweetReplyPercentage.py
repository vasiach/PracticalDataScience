#from __future__ import division
import tweepy
from twitter_config import config


def get_reply_percentage(config, username, max_tweets=100):
    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth)

    tweets = 0
    reply_status = 0

    for status in tweepy.Cursor(api.user_timeline, id=username).items(max_tweets):
        tweets += 1
        if status.in_reply_to_status_id is not None:
            print( status.text)
            reply_status += 1
    return round(((reply_status / tweets) * 100), 1)


screen_name = 'jimmyfallon'
max_tweets = 500

percentage = get_reply_percentage(config, screen_name, max_tweets)
print("The percentage of the tweets that were replies of the user {} is {} ".format(screen_name, percentage))