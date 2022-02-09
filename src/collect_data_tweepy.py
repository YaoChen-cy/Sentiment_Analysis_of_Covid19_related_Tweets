import os
import tweepy as tw
import pandas as pd
import datetime


def main():
    auth = tw.OAuthHandler("XXX", "XXX")
    auth.set_access_token("XXX", "XXX")
    api = tw.API(auth, wait_on_rate_limit=True)

    # get the tweets in a json object
    # get tweets from specfic time range 
    until_date = datetime.datetime(2021, 11, 12, 0)
    # set the keyword the twwets contain
    keyword = "COVID"
    # get tweets from api
    results = [status._json for status in
               tw.Cursor(api.search_tweets, q=keyword, count=100,tweet_mode='extended', lang='en',until=until_date).items(800)]

    # iterate over 'results' and store the complete message from each tweet
    my_tweets = []
    date=[]
    for result in results:
        # get tweets/retweets with full text
        date.append(result["created_at"])
        if (not result["full_text"].startswith("RT")):
            my_tweets.append(result["full_text"])
            
        else:
            my_tweets.append(result["retweeted_status"]["full_text"])
    
    # store the raw data to csv file
    df = pd.DataFrame({'date':date,'text': my_tweets})
    df.to_csv('COVID_Nov11.csv')

    
if __name__ == "__main__":
    main()
