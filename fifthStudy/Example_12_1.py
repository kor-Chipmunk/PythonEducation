import tweepy
import datetime
import json
import threading

consumer_key = "GMxrEcr4vPeG5c0AwP3ACjccA"
consumer_secret = "X695cArv3pFUeXTPaBcnXJsfJxQvKpdKs1QQ3kYNfF3D6z2j1b"

access_token = "823728988250054656-HBaFXA55KkUMAZhFWaIdJahuMhVR8WT"
access_token_secret = "YM6jiUGRFB87wvW0o5mLlJdVB3BGj8RWMM6jQfuBoWNSx"

# consumer_key = "Mavh0qsQUFMpVazkczpkUqQ2e"
# consumer_secret = "O7GfQBPrEaTakSiOEoRieItXb8F7tVNCrrLE08cmesFBKVHq5k"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# access_token = "735344297176879104-2CJiWsBvzFnKMON29Esz1b6dLkXYetE"
# access_token_secret = "gWh5eORC05WPVjffQFbnehwwzdYxX0JCCFDRM6NdUF1nz"

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
count = 20

def advertising():
    global count
    tweet = "♚♚히어로즈 오브 더 스☆톰♚♚가입시$$전원 카드팩☜☜뒷면100%증정※ ♜월드오브 워크래프트♜펫 무료증정￥ 특정조건 §§디아블로3§§★공허의유산★초상화♜오버워치♜겐지스킨{0}￥획득기회@@@ 즉시이동http://kr.battle.net/heroes/ko/".format(count)
    # api.update_status(status=tweet)
    api.update_with_media("bg.jpg", status=tweet)
    count += 1
    print("Advertising : {0}".format(count))
    timer = threading.Timer(2, advertising)
    timer.start()

# advertising()
api.create_friendship("corcorgiBH")
# api.update_profile_image("profile.png")
# api.update_profile_background_image("bg.jpg")

# 트윗 포스트하기
# tweet = str(datetime.datetime.now()) + ' 파이썬 프로그래밍 테스트'
# api.update_status(status=tweet)

# print("Successfully Posted.")
# print() # 빈줄 출력

# 타임 라인 읽어오기
# public_tweets = api.user_timeline()