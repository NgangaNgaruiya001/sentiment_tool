# textblob
# tweepy

from textblob import TextBlob
import tweepy
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


api_key = 'WQXyj3gjHlxXwm0zDx4soFiFV'
api_key_secret = 'VHUVts9L5QWUqIgX14PCwJo1mLnFuglpfKGRElopBVmo9hMgee'

access_token = '747108951997702148-iIgFVvQa80fmI5Ho4LUHfMeiQ1qnAWo'
access_token_secret = 'X33uEiWRddpwdrDAKdsUt3divuWmEECTxlekH53P6fcUu'


auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)




# search_term = 'Mpesa'
# tweet_amount = 10






def sentimentChecker(search_term, tweet_amount):
	polarity = 0
	negative = 0
	positive = 0
	Neutral = 0
	tweets = tweepy.Cursor(api.search_tweets, q=search_term.lower(), lang='en').items(tweet_amount)
	for tweet in tweets:
		clean_tweet = tweet.text.replace('RT', '')
		if clean_tweet.startswith(' @'):
			postion = clean_tweet.index(':')
			clean_tweet = clean_tweet[postion+2:]
		if clean_tweet.startswith('@'):
			postion = clean_tweet.index(' ')
			clean_tweet = clean_tweet[postion+2:]
		clean_tweet = clean_tweet.lower()
		# print(clean_tweet)

		analysis = TextBlob(clean_tweet)
		tweet_polarity = analysis.polarity
		polarity += tweet_polarity

		if tweet_polarity > 0:
			positive += 1
		elif tweet_polarity == 0:
			Neutral += 1
		else:
			negative += 1



	print(polarity)
	print(f'The amount of positive tweets are: {positive}')
	print(f'The amount of neutral tweets are: {Neutral}')
	print(f'The amount of negative tweets are: {negative}')

	polarity = {'Postive': 10,'Neutral': 10 ,'Negative':10}
	df = pd.DataFrame(polarity, index=['Tweet_No']).T.reset_index()


	print(df)

	sns.barplot( x= 'index' ,y='Tweet_No', data = df).set(xlabel='general polarity', title=search_term.upper())


	plt.show()





sentimentChecker('?', 100)