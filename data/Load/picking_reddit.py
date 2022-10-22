import pandas as pd
import numpy as np
import datetime
from pmaw import PushshiftAPI

def main():
    # get epoch of date
    after_time = int(datetime.datetime(2019, 10, 1, 0, 0).timestamp())
    before_time = int(datetime.datetime(2022, 9, 30, 0, 0).timestamp())

    api = PushshiftAPI()

    subreddits = ['ethereum' ,'ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']
    subreddits_posts = dict()

    print("-------------start-------------")
    for subreddit in subreddits:
        print("Beginning search for", subreddit)
        subreddits_posts[subreddit] = api.search_submissions(subreddit=subreddit,
                                            filter=['title','selftext','created_utc','subreddit'],
                                            after=after_time,
                                            before=before_time,                 
                                            #limit=10000,
                                            )
        print("Ended search for", subreddit)
    print("--------------end--------------")


    df = pd.DataFrame()
    for subreddit in subreddits:
        df = pd.concat([df, pd.DataFrame([post for post in subreddits_posts[subreddit]])])
        

    # It is necessary to split df as it is too big.
    result = np.array_split(df, 2)
    
    result[0].to_csv(r'C:\Users\SR118\Desktop\Reddit_1.csv', index = False, header=True)
    result[1].to_csv(r'C:\Users\SR118\Desktop\Reddit_2.csv', index = False, header=True)

if __name__ == "__main__":
    main()