# CRYPTOCURRENCY FORECASTING MODELS
We have developed a double LSTM architecture (Sentiment model + Stock model) for the forecasting of the price of cryptocurrencies. For the model we have two different training methods, with different focus. They can be found in the following files:
- model_short_forecast.ipynb
- model_long_forecast.ipynb

## Short forecast model
This model requires a small amount of epochs to train, and is good at making short term forecasts, being accurate enough in 1 week forecasts.  
In this model we train in batches of 1, it is in timeseries form so gradients are acumulated and we have no need to train saving the hidden state memory.  
##### Saved Models
Saved models can be found in the folder: model/saved_models_S/   
##### Results
Results can be found in the file: model/saved_models_S/README.md  
Graphs can be found in the folder: model/Result_Graphs/short_focused/  

## Long forecast model
This model requires a large amount of epochs to train, at least 100, but you could go for 150 and still find loss reductions. It is way better at making long term forecasts, and if trained correctly, can excel at making next day, 1 week, and up to 50 days (tested) forecasts.  
In this model we train in batches of 256, and for each batch we make a stack for the sentiment, put in a single instance all the stock and sentiment data into the StockPredictor model for the first 206 days, and then run a forecast for the next 50 days. It learns how to use the hidden state memory together with the data to make forecasts.
##### Saved Models
Saved models can be found in the folder: model/saved_models_L/
##### Results
Results can be found in the file: model/saved_models_L/README.md
Graphs can be found in the folder: model/Result_Graphs/long_focused/