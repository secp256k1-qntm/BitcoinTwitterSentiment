Bitcoin Twitter Sentiment Analysis
==================

Program that analyzes sentiment of recent tweets related to Bitcoin and provides recommendation suitable to Bitcoin extremist's point of view.
This is not a financial advice or financial advise generating program. :)

It utilizes vader sentiment analysis tool, tweepy api and a FUD wordlist prepared from past few years of experience in the cryptoo market.
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool is fully open-sourced under the MIT License.  


## Installation 
- __Python:__ Python 3.6 or higher
- __Vader:__ pip install vaderSentiment
- __Tweepy:__ pip install tweepy


##Twitter API keys and token generation

- Go to https://dev.twitter.com/apps
	   If you don't already have an account, you can login with your normal Twitter credentials.
     
- Go to "Create an app"
	   Fill in the details of the application you'll be using to connect with the API
	   Your application name must be unique. If someone else is already using it, you won't be able to register your application until you can think of something that isn't being used.
     
- Create your Twitter application (anything/just a test app)
	   Details of your new app will be shown along with your consumer key and consumer secret.
	   Scroll down and click Create my access token


Existing apps:

To get the consumer and access tokens for an existing application, go to My applications.

### Running the tests

After you have replaced twitter api keys and tokens in Bitcoin_Twitter_Sentiment_Meter.py :

[Bitcoin_Twitter_Sentiment_Meter.py](Bitcoin_Twitter_Sentiment_Meter.py)

python3 Bitcoin_Twitter_Sentiment_Meter.py

Positive tweet percentage 18.0

Negativ  tweet percentage 82.0

FUD at ATH, BTFD

### Authors

* **hodl2020** - *Initial work* - [hodl2020](https://github.com/hodl2020)


### License

This project is fully open-sourced under the MIT License - see the [LICENSE](LICENSE) file for details

