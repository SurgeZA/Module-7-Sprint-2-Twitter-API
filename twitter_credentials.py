# Variables that contain the user credentials to acces twitter API
import tweepy
from tweepy import OAuthHandler
consumer_key = '754438549089452032-IDf01s65TU9kmjl3yBgTSdCzrIcpx3N'
consumer_secret = 'xQeCPkkAEWrOmdCwTieyGJLyVvSwY1UujyR3YA18t1U91'
access_token = '8S5QagaZS7D6fI3kjbWOxxqyL'
access_secret = 'Ym4e0O84XXxt74BBQq2YJgS4pCTsvfrqV6Ghhv08O1wdXY08dM'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)