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
    subreddits = ['ethereum']#,'ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']

    date_range = pd.date_range(start="2019-10-01", end="2022-09-30")
    date_range_list = []
    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    
    print(len(search('ethereum', date_range_list[0], date_range_list[1])))
    #df = search(subreddits)
    #create_csv(df)


# Filter for submission search
def sub_filter(item):
    return item['score'] > 50 #and item['num_comments'] > 100


def search(subreddit, before, after):
    api = PushshiftAPI(num_workers=40,)

    # Submission search
    print("-------------start-------------")
    print("Beginning search for", subreddit)
    s = api.search_submissions(subreddit=subreddit,
            filter=['title','selftext','created_utc','subreddit','score','num_comments'],#,'full_link'],
            #filter_fn=sub_filter,
            after=after,
            before=before,                                                         
                                            )
    print("Ended search for", subreddit)
    print("--------------end--------------")

    return pd.DataFrame(s)
    

def create_csv(df):
    # Split DataFrame
    result = np.array_split(df, 4)
    # Generate csv files
    result[0].to_csv(r'./datasets/Reddit_unfiltered/Reddit_1.csv', index = False, header=True)
    result[1].to_csv(r'./datasets/Reddit_unfiltered/Reddit_2.csv', index = False, header=True)
    result[2].to_csv(r'./datasets/Reddit_unfiltered/Reddit_3.csv', index = False, header=True)
    result[3].to_csv(r'./datasets/Reddit_unfiltered/Reddit_4.csv', index = False, header=True)


if __name__ == "__main__":
    main()