# import data handling tools
import pandas as pd
import numpy as np

# import data visualization tools
import matplotlib.pyplot as plt
import seaborn as sns

# Reddit Data
df_Crypto_Currency_News = pd.read_csv('../Load/Reddit/comments/Crypto_Currency_News_comments.csv')
df_CryptoCurrencies = pd.read_csv('../Load/Reddit/comments/CryptoCurrencies_comments.csv')
df_CryptoCurrency = pd.read_csv('../Load/Reddit/comments/CryptoCurrency_comments.csv')
df_Cryptomarkets = pd.read_csv('../Load/Reddit/comments/Cryptomarkets_comments.csv')
df_eth = pd.read_csv('../Load/Reddit/comments/eth_comments.csv')
df_ethfinance = pd.read_csv('../Load/Reddit/comments/ethfinance_comments.csv')
df_ethtrader = pd.read_csv('../Load/Reddit/comments/ethtrader_comments.csv')

# Yahoo Data
df_yahoo = pd.read_csv('../Load/datasets/Yahoo/ETH-USD.csv', delimiter=';')

# Binanace Data
df_BNB_ETH = pd.read_csv('../Load/datasets/Binance/BNB-ETH-klines.csv', delimiter=';')
df_ETH_BTC = pd.read_csv('../Load/datasets/Binance/ETH-BTC-klines.csv', delimiter=';')
df_ETH_USDT = pd.read_csv('../Load/datasets/Binance/ETH-USDT-klines.csv', delimiter=';')
df_XRP_ETH = pd.read_csv('../Load/datasets/Binance/XRP-ETH-klines.csv', delimiter=';')

# print colnames of reddit data
print(df_Crypto_Currency_News.columns)

# 