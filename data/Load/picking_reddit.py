from ast import Num
import pandas as pd
import numpy as np
import datetime
from pmaw import PushshiftAPI

def main():
    subreddits = ['ethereum']# ,'ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']
    df = search(subreddits)
    creat_csv(df)

    
def sub_filter(item):
    return item['score'] > 100 #and item['num_comments'] > 100


def search(subreddits):
    api = PushshiftAPI(num_workers=40,)
    subreddits_posts = dict()
    after_time = int(datetime.datetime(2019, 10, 1, 0, 0).timestamp())
    before_time = int(datetime.datetime(2022, 9, 30, 0, 0).timestamp())

    print("-------------start-------------")
    for subreddit in subreddits:
        print("Beginning search for", subreddit)
        subreddits_posts[subreddit] = api.search_submissions(subreddit=subreddit,
                                            filter=['title','selftext','created_utc','subreddit','score','full_link','num_comments'],
                                            filter_fn=sub_filter,
                                            after=after_time,
                                            before=before_time,                 
                                            #limit=1000,
                                            #limit=1000,
                                            )
        print("Ended search for", subreddit)
    print("--------------end--------------")
    # join for multiple searches
    df = pd.DataFrame()
    for subreddit in subreddits:
        df = pd.concat([df, pd.DataFrame([post for post in subreddits_posts[subreddit]])])

    return df
    

def creat_csv(df):
    result = np.array_split(df, 2)
    result[0].to_csv(r'C:\Users\SR118\Desktop\Reddit_1_t.csv', index = False, header=True)
    result[1].to_csv(r'C:\Users\SR118\Desktop\Reddit_2_t.csv', index = False, header=True)


if __name__ == "__main__":
    main()