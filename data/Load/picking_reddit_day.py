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
    subreddits = ['ethereum','ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']

    date_range = pd.date_range(start="2019-10-01", end="2022-09-30")
    date_range_list = []
    
    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    
    num_post_list = []
    
    for subreddit in subreddits:
        print("-------------start-------------")
        print("Beginning search for", subreddit)
        for day in date_range_list:
            print("day", day)
            num_post_list.append(len(search(subreddit, day, day+86400)))
            print("end", day)
        print("Ended search for", subreddit)
        print("--------------end--------------")

    df = pd.DataFrame(data={"num_of_sub": num_post_list})
    df.to_csv(r'./datasets/Reddit_sub.csv', sep=',',index=False)
    
    #print(int(datetime.datetime(2019, 10, 1, 0, 0).timestamp()))
    #print(int(datetime.datetime(2019, 10, 2, 0, 0).timestamp()))
    #print(len(search('ethereum', date_range_list[0], date_range_list[1])))
    
def search(subreddit, after, before):
    api = PushshiftAPI(num_workers=40,shards_down_behavior=None,)

    # Submission search
    submissions = api.search_submissions(subreddit=subreddit,
            filter=['title','selftext','created_utc','subreddit','score','num_comments'],#,'full_link'],
            after=after,
            before=before,)
    
    return submissions
    

if __name__ == "__main__":
    main()