import tweepy
import datetime
import json

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# DM Message Object 가져오기
try:
    getDMs = api.direct_messages()

    for dm in getDMs:
        print(json.dumps(dm._json))
except tweepy.TweepError as err:
    print("접근권한이 없습니다.")
    print("{0}".format(err))

# 트윗 포스트하기
# tweet = str(datetime.datetime.now()) + ' 파이썬 프로그래밍 테스트'
# api.update_status(status=tweet)

## print("Successfully Posted.")
## print() # 빈줄 출력

# 타임 라인 읽어오기
## public_tweets = api.user_timeline("BlindRendererKR")
#  print(public_tweets[0]._json)
# for tweet in public_tweets:
#   print(json.dumps(tweet._json))