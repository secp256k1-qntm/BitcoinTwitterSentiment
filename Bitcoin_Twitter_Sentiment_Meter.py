import tweepy
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime

#goto ReadMe for guide on getting your own twitter dev api keys,tokens to replace below
consumer_key = 'XXXXXXXXXXXXXXXXX'  # API Key
customer_secret = 'YYYYYYYYYYYYYYY'  # API Secret Key
access_token = 'ZZZZZZZZZZZZZZ'  # Access token
access_token_secret = 'AAAAAAAAAAAAAAAA' # Access token secret


auth = tweepy.OAuthHandler(consumer_key, customer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def clean_tweet(tweet):
    # function to clean tweet text by removing links, special characters
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


analyzer = SentimentIntensityAnalyzer()
cnt = 0
ncnt = 0
pcnt = 0
fcnt = 0
today = datetime.datetime.now()
# keeping search date range small as I expect to run this on daily frequency
DD = datetime.timedelta(days=3)
earlier = today - DD

earlier = earlier.strftime('%Y-%m-%d')
today = today.strftime('%Y-%m-%d')

#print (earlier,today)


for tweet in tweepy.Cursor(api.search,
                           q="bitcoin",  # Searching for word bitcoin
                           include_entities=False,  # Do not include URLs
                           since=earlier,  # Start date
                           until=today,  # Till date
                           lang="en").items(100):  # Language english and tweet limit 25
    if cnt > 100:
        break
    ctweet = clean_tweet(tweet.text)
    txt = analyzer.polarity_scores(ctweet)
    cnt += 1
    if (txt['compound'] < -0.1):
        # uncomment this if you wish to see tweet text
        #print('Negative '+ ctweet)
        ncnt += 1
        # List of common FUD in media
        # fudRegex is not made dynamic for specific reason. These are the social attack vectors which marked the bottom of the trend and you would have been safer buying in that zone then later selling on peak euphoria. Ask nouriel lol
        fudRegex = re.compile(r'death spiral|obituary|market is dead|bitcoin flashcrash|bitcoin banned|ban on bitcoin|end of bitcoin|bitcoin funeral|china bans|korea bans|bitcoin is fraud|etf reject|btc hardfork|bitcoin died|bitcoin bloodbath|crypto hell|bitcoin nightmare', re.IGNORECASE)
        fud = fudRegex.search(ctweet)
        if fud is not None:
            # print(fud.group()) #uncomment to see which FUD word hit
            fcnt += 1
    else:
        # print('Positive '+ ctweet)  #uncomment this if you wish to see tweet text
        pcnt += 1


print('\nPositive tweet percentage ' + str(round(100*pcnt/cnt, 2)))
print('\nNegative tweet percentage ' + str(round(100*ncnt/cnt, 2)))

if round(100*ncnt/cnt, 2) > 50:
        print('\nGreat time to go bargain hunting some bitcoins')
if round(100*fcnt/cnt, 2) > 5:
        print('\nFUD at ATH, BTFD')
