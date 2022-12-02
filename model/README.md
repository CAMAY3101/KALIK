# CRYPTOCURRENCY FORECASTING MODELS
We have developed a double LSTM architecture (Sentiment model + Stock model) for the forecasting of the price of cryptocurrencies. For the model we have two different training methods, with different focus. They can be found in the following files:
- model_short_forecast.ipynb
- model_long_forecast.ipynb

---
## Short forecast model
This model requires a small amount of epochs to train, and is good at making short term forecasts, being accurate enough in 1 week forecasts.  
In this model we train in batches of 1, it is in timeseries form so gradients are acumulated and we have no need to train saving the hidden state memory.  

### Saved Models
Saved models can be found in the folder: saved_models_S/  
##### Best Models:
- Model 01_01 - Crypto_Currency_News
  - Overal highest amount of first week price closes (ETH to USD, BTC, BNB, XRP) within 0.3 STDs of real value, falls of in second week.
- Model 01_05 - eth
  - Good one week forecast with adj_close ETH-USD within 0.3 STDs of real value, two week close_BTC all within .3 STDs of real value.
- Model 01_07 - ethtrader
  - Great one week and two week forecast accuracies, all adj_close ETH-USD within 0.3 STDs of real value.

### Results
Results can be found in the file: saved_models_S/README.md  
Graphs can be found in the folder: Result_Graphs/short_focused/  

## Long forecast model
This model requires a large amount of epochs to train, at least 100, but you could go for 150 and still find loss reductions. It is way better at making long term forecasts, and if trained correctly, can excel at making next day, 1 week, and up to 50 days (tested) forecasts.  
In this model we train in batches of 256, and for each batch we make a stack for the sentiment, put in a single instance all the stock and sentiment data into the StockPredictor model for the first 206 days, and then run a forecast for the next 50 days. It learns how to use the hidden state memory together with the data to make forecasts.

### Saved Models
Saved models can be found in the folder: saved_models_L/
##### Best Model:
- Model 30_01 - Crypto_Currency_News
  - Trained for the longest time, best accuracy in training data, forecasts of 5 batches, and forecast of extra week.

### Results
Results can be found in the file: saved_models_L/README.md  
Graphs can be found in the folder: Result_Graphs/long_focused/

---
### Indicators of Model Performance
Our metric for evaluation is how many predictions are within 0.3 standard deviations of the real value. We aply this metric separately for in-training predictions and for forecasts.

We receive in percentages this amount for each variable: adj_close, volume, num_trades_USDT, close_BTC, num_trades_BTC, close_BNB, num_trades_BNB, close_XRP, num_trades_XRP.

It is to note that some variables are not important to predict, but we keep as they can be explicative for others in the model learning, being volume, num_trades_USDT, num_trades_BTC, num_trades_BNB and num_trades_XRP.

Where we want high percentages are in the forecasts within 0.3 stds of the real value for: adj_close, close_BTC, close_BNB and close_XRP. With adj_close being the most important.
