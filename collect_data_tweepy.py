import os
import tweepy as tw
import pandas as pd
import json
import datetime

def main():
    auth = tw.OAuthHandler("9vJ7ziTtCqL14ndcDxzGM4wAb", "CXDxYOqw7mGWVDOYpoSaFE6YeIF5PXz67IY2gAEOmvRr46XKoj")
    auth.set_access_token("1459917468441497604-E4S9SmZUPAfHw9zGixsiburv1gv7LR", "yxJRIemlaDqKgS1MYOW4u1rCBYQsFLUOq2vM9DYaZlARW")
    api = tw.API(auth, wait_on_rate_limit=True)

    since_date = '2021-11-11'
    until_date = '2021-11-12'
    # get the tweets in a json object
    startDate = datetime.datetime(2021, 11, 11, 0, 0, 0)
    results = [status._json for status in
               tw.Cursor(api.search_tweets, q="covid", tweet_mode='extended', lang='en',until=until_date).items(50)]
    """
    with open("sample.json","w") as file:
        for post in results:
            print(post["created_at"])
    """
    # iterate over 'results' and store the complete message from each tweet.
    my_tweets = []
    date=[]
    for result in results:
        date.append(result["created_at"])
        if (not result["full_text"].startswith("RT")):
            my_tweets.append(result["full_text"])
            
        else:
            my_tweets.append(result["retweeted_status"]["full_text"])

    df = pd.DataFrame({'date':date,'text': my_tweets})
    df.to_csv('file_name.csv')
    

if __name__ == "__main__":
    main()
