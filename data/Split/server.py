from pymongo import MongoClient
import pandas as pd
#import os

#entries = os.listdir('../Load/datasets/')
#print(entries)
df_Binance = pd.read_csv('../Load/datasets/Binance.csv')
print(df_Binance.columns)
df_eth = pd.read_csv('../Load/datasets/ETH-USD.csv')
print(df_eth.columns)
df_reddit = pd.read_csv('../Load/datasets/Reddit_filtered/Reddit_1.csv')
print(df_reddit.columns)