import requests
import os
import json


bearer_token = "XXX"
search_url = "https://api.twitter.com/2/tweets/search/recent"


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "XXX"
    return r

def create_url(keyword, start_date, end_date, max_results=10):
    # set the endpoint the collect data from
    search_url = "https://api.twitter.com/2/tweets/search/recent" 

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
