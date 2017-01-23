import tweepy
import datetime
import json

consumer_key = "72Zz59EYsXK0EtwERLKDrHu7V"
consumer_secret = "MOeqwJ6eiKyCDV8QwhLJExezyoY6Wn7SufBIpwR8BBXmvQ6Rqw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "735344297176879104-2CJiWsBvzFnKMON29Esz1b6dLkXYetE"
access_token_secret = "gWh5eORC05WPVjffQFbnehwwzdYxX0JCCFDRM6NdUF1nz"

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# 트윗 포스트하기
# tweet = str(datetime.datetime.now()) + ' 파이썬 프로그래밍 테스트'
# api.update_status(status=tweet)

print("Successfully Posted.")
print() # 빈줄 출력

# 타임 라인 읽어오기
public_tweets = api.user_timeline("BlindRendererKR")
print(public_tweets[0]._json)
# for tweet in public_tweets:
#   print(json.dumps(tweet._json))