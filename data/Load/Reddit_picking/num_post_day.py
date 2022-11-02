"""
Author: Maximiliano Martínez Márquez
Project: Sentiment Analysis For CryptoCurrency Forecasting
app: Data Transformation
"""

# DataFrame manipulation
import pandas as pd
# Split DataFrame
import numpy as np
# Get before and after Epochs for search submissions function 
import datetime
# Wrapper for the Pushshift API used to retrieve Reddit submissions
from pmaw import PushshiftAPI

"""
Obtain data from various subreddits and generate a csv file.
How to run file:
(Open Kalik folder)
cd data
cd Load
python picking_reddit.py
"""

def main():
    # List of subreddits used to retrieve submissions
    subreddits = ['ethereum',]#'ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']

    date_range = pd.date_range(start="2019-10-01", end="2022-09-30")
    date_range_list = []
    
    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    
    df = pd.DataFrame()
    num_post_list = []

    for subreddit in subreddits:
        print("-------------start-------------")
        print("Beginning search for", subreddit)
        for day in date_range_list:
            r = search(subreddit, day, day+86400)
            if len(r) == 0:
                r = search(subreddit, day, day+86400)
            num_post_list.append(r)
            df = pd.concat([df, pd.DataFrame(r)])

    df = pd.DataFrame(data={"num_of_post": num_post_list})
    df.to_csv(r'num_post_day.csv', sep=',',index=False)
    
def search(subreddit, after, before):
    api = PushshiftAPI(num_workers=40,shards_down_behavior=None,rate_limit=30,)

    # Submission search
    submissions = api.search_submissions(subreddit=subreddit,
            filter=[],
            after=after,
            before=before,)

    return len(submissions)
    

if __name__ == "__main__":
    main()