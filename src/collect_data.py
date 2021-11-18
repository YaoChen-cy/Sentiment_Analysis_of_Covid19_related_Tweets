import requests
import os
import json


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
#bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPslVwEAAAAAoq4VtVHgfC63HpcbcEMKUJCK5Eo%3Dboec4QGn0PfbTgt1M0ecXf3x9At7jzj5KTINineTf7QPECdn6R"


search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
#query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "COMP598_Final_Project_AAA"
    return r

def create_url(keyword, start_date, end_date, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/recent" # Change to the endpoint you want to collect data from

    # change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'geo.place_id',
                    'tweet.fields': 'text,created_at,lang,geo',
                    'place.fields': 'country',
                    'next_token': {}
                    }
    return (search_url, query_params)

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    keyword = "(Covid Vaccine) (lang:en)"
    start_time = "2021-11-09T00:00:00.000Z"
    end_time = "2021-11-13T00:00:00.000Z"
    max_results = 10
    url = create_url(keyword, start_time, end_time, max_results)
    json_response = connect_to_endpoint(url[0], url[1])
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
