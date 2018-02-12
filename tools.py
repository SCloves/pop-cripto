import twitter
import os

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token_key= os.environ['access_token_key']
access_token_secret = os.environ['access_token_secret']

api_twitter = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

criptoMoedas = ['bitcoin', 'litecoin', 'Ethereum']

def getCripto(text):
    for m in criptoMoedas:
        if m in text.lower():
            return m
    else:
        return False

dic = {'bitcoin': 0, 'litecoin': 0, 'Ethereum': 0}
for tw in api_twitter.GetStreamFilter(track=criptoMoedas):
    try:
    	key = getCripto(tw['text'])
    	if key:
        	dic[key] += 1
        else:
        	continue
    except:
        continue

