import csv
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

query = "binus"
language = "id"

results = api.search(q=query, count=100)

csvFile = open('binus.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in results:
    display = tweet.user.screen_name, "Tweeted:",tweet.text
    print(display)
    csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.text])