import config
import json
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, AS)

url = "https://api.twitter.com/1.1/statuses/update.json"

# コマンドラインに入力したものをツイートする
tweet = input('>>')

# statusはツイートする内容
param = {"status" : tweet}

res  = twitter.post(url, params = param)

if res.status_code == 200:
    print('success')
else:
    print('faild status_code:{}'.format(res.status_code))