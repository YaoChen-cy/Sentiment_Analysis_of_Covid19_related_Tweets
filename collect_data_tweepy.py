import os
import tweepy as tw
import pandas as pd
def main():
    auth = tw.OAuthHandler("9vJ7ziTtCqL14ndcDxzGM4wAb", "CXDxYOqw7mGWVDOYpoSaFE6YeIF5PXz67IY2gAEOmvRr46XKoj")
    auth.set_access_token("1459917468441497604-E4S9SmZUPAfHw9zGixsiburv1gv7LR", "yxJRIemlaDqKgS1MYOW4u1rCBYQsFLUOq2vM9DYaZlARW")
    api = tw.API(auth, wait_on_rate_limit=True)

    # get the tweets in a json object
    results = [status._json for status in
               tw.Cursor(api.search_tweets, q="covid", tweet_mode='extended', lang='en').items(5)]

    # iterate over 'results' and store the complete message from each tweet.
    my_tweets = []
    for result in results:
        if (not result["full_text"].startswith("RT")):
            my_tweets.append(result["full_text"])
        else:
            my_tweets.append(result["retweeted_status"]["full_text"])

    df = pd.DataFrame({'text': my_tweets})
    df.to_csv('file_name.csv')

if __name__ == "__main__":
    main()
