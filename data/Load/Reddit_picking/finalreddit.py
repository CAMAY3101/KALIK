import datetime
import random
import time
import praw
import pandas as pd
import requests
"""
import uuid
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
"""
"""
https://api.pushshift.io/reddit/search/submission/?subreddit=ethereum&size=10&fields=subreddit,title,score,permalink,created_utc,subreddit_id&sort=desc&sort_type=score&after=1569906000&before=1569992400
"""

"""
TODO:
1. create function to get dataframe from csv
2. create function to get post id from dataframe
3. append comment body and comment score? to dataframe?
4. create whole csv file for each comment?
5. create function to get all post id from api
"""

"""
If going to test the code, please change csv file name to avoid overwriting
"""
def main():
    #subreddits = ['ethereum','ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']
    subreddits = ['ethereum']
    start = "2019-10-01"
    #end = "2022-09-30"
    end = "2019-10-14"
    date_range_list = get_date_range(start, end)

    start_time = time.perf_counter()
    #submissions = get_submissions(subreddits, date_range_list)
    post_id = get_post_id(subreddits, start, end)
    finish_time = time.perf_counter()
    
    # print the json data
    #print(json.dumps(r, indent=4))
    
    #submissions.to_csv(r'finaltest.csv', sep=',',index=False) 
    post_id.to_csv(r'id.csv', sep=',',index=False) 
    print(f"Program finished in {finish_time-start_time} seconds")
    

"""
returns reddit object to get top comment
"""
def get_praw():
    reddit = praw.Reddit(
    client_id = "1s9rwR-kIsBTTh-nZBO7JA",
    client_secret = "HhrjDoYqItKREVXCWB7OzaRcAvoCwg",
    username = "Longjumping_Day337",
    password = "kalik123",
    user_agent = "my agent",
    )
    return reddit

"""
returns top comment for sumbission id

example: get_top_comment("dbruyz")

example 2:
for sub_id in data["data"]:
    print(sub_id)
    submission_praw = reddit.submission(id=sub_id)
    submission_praw.comment_sort = "top"
    print(submission_praw.comments[0].body)

Typical attributes of a comment are listed in link below:
- https://praw.readthedocs.io/en/stable/code_overview/models/comment.html
"""
def get_top_comment(reddit, sumbission_id):
    try:
        sub = reddit.submission(id=sumbission_id)
    except Exception as e:
        print(e)
    sub.comment_sort = "top"
    return sub.comments[0]

"""
Creates a request to pushshift api and returns a json object with the top ten posts found
Uses tag (function name) to determine which params to use
"""
def get_data(**kargs):
    url = "https://api.pushshift.io/reddit/search/submission/"
    params = {}
    if kargs.get("tag") == "get_submissions":
        params = {
            "subreddit": kargs.get("subreddit"),
            "size": kargs.get("size"),
            "fields": kargs.get("fields"),
            "sort": kargs.get("sort"),
            "sort_type": kargs.get("sort_type"),
            "after": kargs.get("after"),
            "before": kargs.get("before"),
        }
    elif kargs.get("tag") == "get_post_id":
        params = {
            "subreddit": kargs.get("subreddit"),
            #"limit": kargs.get("limit"),
            "size": kargs.get("size"),
            "fields": kargs.get("fields"),
            "sort_type": "created_utc",
            "after": kargs.get("after"),
            "before": kargs.get("before"),
        }
    else:
        return None
    
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts:
        try:
            r = requests.get(url, params=params)
            return r.json()
        except requests.exceptions.RequestException as e:
            attempts += 1
            print(f"Error: {e}")
            print(f"Retrying... {attempts}/{max_attempts}")
            time.sleep((2 ** attempts) + random.random())
    

"""
Return dataframe containing top 10 posts in a day for each subreddit
only works with list of days!!!
"""
def get_submissions(subreddits, date_range_list):
    df = pd.DataFrame()
    l = len(date_range_list)
    for subreddit in subreddits:
        d = 0
        for day in date_range_list:
                data = get_data(tag="get_submissions",
                    subreddit=subreddit,
                    size=10,
                    fields=["subreddit", "title", "score", "num_comments", "permalink", "created_utc", "id"],
                    sort="desc",
                    sort_type="score",
                    after=day,
                    before=day+86400)
                df = pd.concat([df, pd.DataFrame(data["data"])])
                d += 1
                print(d, l)
    return df

def get_post_id(subreddits, after, before):
    df = pd.DataFrame()
    for subreddit in subreddits:
        data = get_data(tag="get_post_id",
            subreddit=subreddit,
            #limit=None,
            size=1000,
            fields=["subreddit","id"],
            after=after,
            before=before)
        df = pd.concat([df, pd.DataFrame(data["data"])])
                
    return df
"""
Return a list of days in unix time stamp
"""
def get_date_range(start, end):
    date_range = pd.date_range(start=start, end=end, freq="D")
    date_range_list = []

    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    return date_range_list


if __name__ == '__main__':
    main()


"""
url_list = ['https://api.pushshift.io/reddit/search/submission/?subreddit=wallstreetbets&sort=desc&sort_type=score&size=10&after=7d&fields=score,title', 
            'https://api.pushshift.io/reddit/search/submission/?q=wallstreetbets']

def download_file(url, file_name):
    try:
        html = requests.get(url, stream=True)
        #js = json.loads(html.json())
        #print(json.dumps(js, ident=4))
        open(f'{file_name}.json', 'wb').write(html.content)
        return html.status_code
    except requests.exceptions.RequestException as e:
        return e

def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for url in url_list:
            file_name = uuid.uuid1()
            threads.append(executor.submit(download_file, url, file_name))
            
        for task in as_completed(threads):
            print(task.result()) 

"""