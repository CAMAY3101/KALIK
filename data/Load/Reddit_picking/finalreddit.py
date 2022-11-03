import datetime
import random
import time
import pandas as pd
import requests
import uuid
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
https://api.pushshift.io/reddit/search/submission/?subreddit=ethereum&size=10&fields=subreddit,title,score,permalink,created_utc,subreddit_id&sort=desc&sort_type=score&after=1569906000&before=1569992400
"""

def get_data(**kargs):
    url = "https://api.pushshift.io/reddit/search/submission/"
    params = {
        "subreddit": kargs.get("subreddit"),
        "size": kargs.get("size"),
        "fields": kargs.get("fields"),
        "sort": kargs.get("sort"),
        "sort_type": kargs.get("sort_type"),
        "after": kargs.get("after"),
        "before": kargs.get("before"),
    }
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
    


def main():
    subreddits = ['ethereum','ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']
    date_range = pd.date_range(start="2019-10-01", end="2022-09-30")
    date_range_list = []

    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))

    d = 0
    l = len(date_range_list)
    df = pd.DataFrame()

    start_time = time.perf_counter()
    for subreddit in subreddits:
        d = 0
        for day in date_range_list:
                data = get_data(subreddit=subreddit,
                    size=10,
                    fields=["subreddit", "title", "score", "num_comments", "permalink", "created_utc", "id"],
                    sort="desc",
                    sort_type="score",
                    after=day,
                    before=day+86400)
                df = pd.concat([df, pd.DataFrame(data["data"])])
                d += 1
                print(d, l)
    
    
    # print the json data
    #print(json.dumps(r, indent=4))
    print(df)
    df.to_csv(r'finaltest.csv', sep=',',index=False) # Change name of csv file
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")
    print(len(df))

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