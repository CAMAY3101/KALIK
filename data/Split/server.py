from pymongo import MongoClient
import pandas as pd
import os

#-------------------FUNCTIONS-------------------#



#-------------------CHECK VARIABLES-------------------#
df_Binance = pd.read_csv('../Load/datasets/Binance.csv')
print("-------------------Binance-------------------")
print(df_Binance.head(5))
df_eth = pd.read_csv('../Load/datasets/ETH-USD.csv')
print("-------------------ETH-USD-------------------")
print(df_eth.head(5))
df_reddit = pd.read_csv('../Load/datasets/Reddit_filtered/Reddit_1.csv')
print("-------------------Reddit-------------------")   
print(df_reddit.head(5))
#-------------------FIX VARIABLES-------------------#
df_eth = df_eth['date;adj_close;volume'].str.split(';', expand=True) #split dataset
df_eth.columns = ['date', 'adj_close', 'volume'] #rename columns
print(df_eth.head(5))
