# coding=utf-8
import tweepy
from textblob import TextBlob

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#word example.words
#sentences example.sentences

print("¿Sobre que termino deseas buscar info?")
palabra = input()
public_tweets = api.search(palabra)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
       print 'POSITIVO'
       print "  "
    elif analysis.sentiment[0]<0:
       print 'MALO'
       print " "
    else:
       print 'NEUTRAL'
       print " "