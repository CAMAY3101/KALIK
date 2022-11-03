"""
Author: Maximiliano Martínez Márquez
Project: Sentiment Analysis For CryptoCurrency Forecasting
app: Data Transformation
"""

import pandas as pd
import numpy as np
import datetime
import time
from pmaw import PushshiftAPI

"""
Como ejecutar el programa
(In Kalik folder directory)
cd data/Load/Reddit_picking
python post_day_10.py
"""
"""
Que cambiar del archivo:
En subreddits (linea 36) cambiar subreddit por su subreddit correspondiente. (Correr uno por uno) 
- Aylin: ethereum, ethtrader 
- Cano: ethfinance, AllCryptoBets
- Max: CryptoCurrency, Crypto_Currency_News
- Gil: CryptoCurrencies, CryptoMarkets
Consideraciones:
- Que no se apague la compu o entre en modo dormir
- En linea 63 cambiar el nombre del archivo csv por el subreddit que corresponda
- Que no se corte la conexion a internet
- El programa tarda aproximadamente 12 horas en correr
"""


def main():
    # List of subreddits used to retrieve submissions
    subreddits = ['CryptoCurrency',] #Change subreddit here
    #'ethtrader', 'ethfinance' 'AllCryptoBets', 'CryptoCurrency', 'Crypto_Currency_News', 'CryptoCurrencies', 'CryptoMarkets']

    date_range = pd.date_range(start="2019-10-01", end="2022-09-30")
    date_range_list = []
    
    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    
    df = pd.DataFrame()
    start = time.perf_counter()
    d = 0
    l = len(date_range_list)
    print(l)
    print(date_range_list)
    for subreddit in subreddits:
        print("-------------start-------------")
        print("Beginning search for", subreddit)
        for day in date_range_list:
            r = search(subreddit, day, day+86400)
            if len(r) == 0:
                r = search(subreddit, day, day+86400)
            df = pd.concat([df, pd.DataFrame(r)])
            d += 1
            print(d, l)
        print("Ended search for", subreddit)
        print("--------------end--------------")
    finish = time.perf_counter()
    df.to_csv(r'cryptocurrency_day_10.csv', sep=',',index=False) # Change name of csv file
    print(f"Program finished in {finish-start} seconds")
    
def search(subreddit, after, before):
    api = PushshiftAPI(num_workers=40,shards_down_behavior=None,rate_limit=30,)

    # Submission search
    submissions = api.search_submissions(subreddit=subreddit,
            filter=['title','created_utc','subreddit','score','num_comments'],#,'full_link'],
            sort_type="score",
            size=10,
            after=after,
            before=before,)
    
    sub_list = [post for post in submissions]

    return sub_list
    

if __name__ == "__main__":
    main()