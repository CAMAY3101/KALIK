"""
Author: Maximiliano Martínez Márquez
Project: Sentiment Analysis For CryptoCurrency Forecasting
app: Data Transformation
"""

import random
import pandas as pd
import numpy as np
import requests
import datetime
import time
from pmaw import PushshiftAPI

"""
Como ejecutar el programa
(In Kalik folder directory)
cd data/Load/Reddit_picking
python post_day_10.py
"""

def main():
    #subreddits = ['ethereum','ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']
    subreddits = ['AllCryptoBets']
    start = "2019-10-01"
    end = "2022-09-30"
    #end = "2019-10-10"
    date_range_list = get_date_range(start, end)

    start_time = time.perf_counter()
    
    #df.to_csv(r'ethtrader_comments.csv', sep=',',index=False) 
    #submissions = get_submissions(subreddits, date_range_list)
    post_id = get_post_id(subreddits, date_range_list)
    finish_time = time.perf_counter()
    print(post_id)
    # print the json data
    #print(json.dumps(r, indent=4))
    
    #submissions.to_csv(r'finaltest.csv', sep=',',index=False) 
    post_id.to_csv(r'AllCryptoBets_id.csv', sep=',',index=False) 
    print(f"Program finished in {finish_time-start_time} seconds")
    
    

def get_data(**kargs):
    url = "https://api.pushshift.io/reddit/search/submission/"
    params = {
        "subreddit": kargs.get("subreddit"),
        "size": kargs.get("size"),
        "fields": kargs.get("fields"),
        "sort_type": "created_utc",
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

def get_post_id(subreddits, date_range_list):
    df = pd.DataFrame()
    l = len(date_range_list)
    for subreddit in subreddits:
        d = 0
        for day in date_range_list:
            data = get_data(
                subreddit=subreddit,
                size=500,
                fields=["subreddit","id"],
                after=day,
                before=day+86400*5)
            df = pd.concat([df, pd.DataFrame(data["data"])])            
            d+=1
            print(f"Subreddit: {subreddit} - {d}/{l}")
    return df

def get_date_range(start, end):
    date_range = pd.date_range(start=start, end=end, freq="5D")
    date_range_list = []

    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    return date_range_list
    
if __name__ == "__main__":
    main()