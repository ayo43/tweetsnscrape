# Importing the packages
import snscrape.modules.twitter as sntwitter
import pandas as pd


query = "(pound) until:2022-06-10 since:2022-01-01"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

data = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

data.to_csv(r'C:\Users\Ayobamidele\Desktop\Match\tweets1.csv')