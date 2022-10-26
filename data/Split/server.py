from ast import Return
from pymongo import MongoClient
import pandas as pd
import os

#-------------------FUNCTIONS-------------------#
def convert_to_dict(dataframe):
    return dataframe.to_dict('records')

def fix_dataframes(dataframe):
    col = dataframe.columns[0]
    cols_names = col.split(";")
    dfNew = dataframe[col].str.split(';', expand=True)  # split dataset
    dfNew.columns = cols_names  # rename columns
    return dfNew

#-------------------DATAFRAMES-------------------#
df_ETH_BTC_BINANCE = pd.read_csv('../Load/datasets/Binance/ETH-BTC-klines.csv')
df_ETH_USDT_BINANCE = pd.read_csv('../Load/datasets/Binance/ETH-USDT-klines.csv')
df_BNB_ETH_BINANCE = pd.read_csv('../Load/datasets/Binance/BNB-ETH-klines.csv')
df_XRP_ETH_BINANCE = pd.read_csv('../Load/datasets/Binance/XRP-ETH-klines.csv')
df_ETH_USD_Yahoo = pd.read_csv('../Load/datasets/Yahoo/ETH-USD.csv')

#-------------------FIX DATAFRAMES-------------------#
df_ETH_BTC_BINANCE = fix_dataframes(df_ETH_BTC_BINANCE)
df_ETH_USDT_BINANCE = fix_dataframes(df_ETH_USDT_BINANCE)
df_BNB_ETH_BINANCE = fix_dataframes(df_BNB_ETH_BINANCE)
df_XRP_ETH_BINANCE = fix_dataframes(df_XRP_ETH_BINANCE)
df_ETH_USD_Yahoo = fix_dataframes(df_ETH_USD_Yahoo)

#-------------------CONVERT TO JSON-------------------#
json_ETH_BTC_BINANCE = convert_to_dict(df_ETH_BTC_BINANCE)
json_ETH_USDT_BINANCE = convert_to_dict(df_ETH_USDT_BINANCE)
json_BNB_ETH_BINANCE = convert_to_dict(df_BNB_ETH_BINANCE)
json_XRP_ETH_BINANCE = convert_to_dict(df_XRP_ETH_BINANCE)
json_XRP_ETH_BINANCE = convert_to_dict(df_XRP_ETH_BINANCE)
json_ETH_USD_Yahoo = convert_to_dict(df_ETH_USD_Yahoo)

#-------------------CONECCTION TO MONGODB-------------------#
client = MongoClient("mongodb+srv://kalikTeam:NietosDeGauss@cluster0.uhbfdme.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('input-kalik')

#-------------------SELECT COLLECTIONS -------------------#
coll_ETH_BTC_BINANCE = db.ETH_BTC_BINANCE
coll_ETH_USDT_BINANCE = db.ETH_USDT_BINANCE
coll_BNB_ETH_BINANCE = db.BNB_ETH_BINANCE
coll_XRP_ETH_BINANCE = db.XRP_ETH_BINANCE
coll_ETH_USD_Yahoo = db.ETH_USD_Yahoo

#-------------------INSERT DATA-------------------#

#NOTE: If you want to insert data, you must delete the collection first. Run the following code just once.

coll_ETH_BTC_BINANCE.insert_many(json_ETH_BTC_BINANCE)
coll_ETH_USDT_BINANCE.insert_many(json_ETH_USDT_BINANCE)
coll_BNB_ETH_BINANCE.insert_many(json_BNB_ETH_BINANCE)
coll_XRP_ETH_BINANCE.insert_many(json_XRP_ETH_BINANCE)
coll_ETH_USD_Yahoo.insert_many(json_ETH_USD_Yahoo)
