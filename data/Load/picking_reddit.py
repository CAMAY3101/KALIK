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
python picking_reddit.py
"""

def main():
    # List of subreddits used to retrieve submissions
    subreddits = ['ethereum','ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']
    df = search(subreddits)
    create_csv(df)


# Filter for submission search
def sub_filter(item):
    return item['score'] > 50 #and item['num_comments'] > 100


def search(subreddits):
    api = PushshiftAPI(num_workers=40,)

    # Dicionary for submission results
    subreddits_posts = dict()

    # Dates to epoch
    after_time = int(datetime.datetime(2019, 10, 1, 0, 0).timestamp())
    before_time = int(datetime.datetime(2022, 9, 30, 0, 0).timestamp())

    # Submission search
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
    

def create_csv(df):
    # Split DataFrame
    result = np.array_split(df, 4)
    # Generate csv files
    result[0].to_csv(r'./datasets/Reddit_1.csv', index = False, header=True)
    result[1].to_csv(r'./datasets/Reddit_2.csv', index = False, header=True)
    result[2].to_csv(r'./datasets/Reddit_3.csv', index = False, header=True)
    result[3].to_csv(r'./datasets/Reddit_4.csv', index = False, header=True)


if __name__ == "__main__":
    main()