from pymongo import MongoClient
import pandas as pd
import os

#-------------------FUNCTIONS-------------------#

#-------------------VARIABLES-------------------#
df_Binance = pd.read_csv('../Load/datasets/Binance.csv')
# print("-------------------Binance-------------------")
# print(df_Binance.head(5))
df_eth = pd.read_csv('../Load/datasets/ETH-USD.csv')
# print("-------------------ETH-USD-------------------")
# print(df_eth.head(5))
df_reddit = pd.read_csv('../Load/datasets/Reddit_filtered/Reddit_1.csv')
# print("-------------------Reddit-------------------")   
# print(df_reddit.head(5))

#-------------------FIX VARIABLES-------------------#
df_eth = df_eth['date;adj_close;volume'].str.split(';', expand=True) #split dataset
df_eth.columns = ['date', 'adj_close', 'volume'] #rename columns
print(df_eth.head(5))

#-------------------CONECCTION TO MONGODB-------------------#
client = MongoClient("mongodb+srv://kalikTeam:NietosDeGauss@cluster0.uhbfdme.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('input-kalik')
eth_usd_info = db.ETH_USD_Yahoo
print(eth_usd_info.count_documents({}))
