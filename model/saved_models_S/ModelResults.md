# Train Test Model Results
Previous versions to 01_01 of the model are deprecated. Production in controlled environment.

These models are good at predicting the close prices in short term, trend to be right in one week forecasts (UP or DOWN). After the last day of training it makes a forecast that either goes up or down, which is an indicator of if the ETH-USD close (also ETH-BTC, BNB-ETH and XRP-ETH closes) is going to go up or down the following days.

---
# Summary of Final Models:
For more detail on each, see the rest of the file.

First week Forecasts within 0.3 standard deviations of actual value, refers to how many (%) of the forcasted values of the first week are at 0.3 or less estandar deviations from the real value.

[Model 01_01 - Crypto_Currency_News](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_01--stock_01_01---crypto_currency_news)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 100.00%
- close_BTC: 85.71%
- close_BNB: 71.43%
- close_XRP: 100.00%

[Model 01_02 - CryptoCurrencies](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_02--stock_01_02---cryptocurrencies)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 85.71%
- close_BTC: 71.43%
- close_BNB: 28.57%
- close_XRP: 100.00%

[Model 01_03 - CryptoCurrency](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_03--stock_01_03---cryptocurrency)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 85.71%
- close_BTC: 100.00%
- close_BNB: 71.43%
- close_XRP: 100.00%

[Model 01_04 - Cryptomarkets](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_04--stock_01_04---cryptomarkets)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 100.00%
- close_BTC: 57.14%
- close_BNB: 42.86%
- close_XRP: 100.00%

[Model 01_05 - eth](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_05--stock_01_05---eth)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 100.00%
- close_BTC: 100.00%
- close_BNB: 28.57%
- close_XRP: 71.43%

[Model 01_06 - ethfinance](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_06--stock_01_06---ethfinance)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 85.71%
- close_BTC: 85.71%
- close_BNB: 71.43%
- close_XRP: 100.00%

[Model 01_07 - ethtrader](https://github.com/CAMAY3101/KALIK/blob/Model-Testing/model/saved_models_S/ModelResults.md#senti_01_07--stock_01_07---ethtrader)  
#### First week Forecasts within 0.3 standard deviations of actual value:
- adj_close: 91.03%
- close_BTC: 92.32%
- close_BNB: 78.82%
- close_XRP: 90.10%

---
### Standard deviations for each column (unnormalized):
- adj_close:       1337.4726991204095 *Main point of interest, ETH-USD listed on Yahoo Finance*
- volume:          10211521929.269737
- num_trades_USDT: 631839.7406452631
- close_BTC:       0.022021368239816732 *Also very important, ETH-BTC listed on Binance*
- num_trades_BTC:  132399.17157028607
- close_BNB:       0.04479372888523323 *BNB-ETH listed on Binance*
- num_trades_BNB:  32263.902864333828
- close_XRP:       0.0004365633549043587 *XRP-ETH listed on Binance*
- num_trades_XRP:  12662.067767368158

---
# Senti_01_01 | Stock_01_01 - Crypto_Currency_News
### Predictions within 0.3 standard deviations of actual value:
[986, 510, 571, 1009, 504, 857, 595, 985, 603] out of 1081
- adj_close: 91.21%
- volume: 47.18%
- num_trades_USDT: 52.82%
- close_BTC: 93.34%
- num_trades_BTC: 46.62%
- close_BNB: 79.28%
- num_trades_BNB: 55.04%
- close_XRP: 91.12%
- num_trades_XRP: 55.78%  
Average All: 68.04%  
Average Closes: 88.74%  

### First week Forecasts within 0.3 standard deviations of actual value:
[7, 4, 4, 6, 1, 5, 6, 7, 0] out of 7
- adj_close: 100.00%
- volume: 57.14%
- num_trades_USDT: 57.14%
- close_BTC: 85.71%
- num_trades_BTC: 14.29%
- close_BNB: 71.43%
- num_trades_BNB: 85.71%
- close_XRP: 100.00%
- num_trades_XRP: 0.00%  
Average All: 63.49%  
Average Closes: 89.29%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[8, 8, 9, 6, 1, 5, 6, 14, 1] out of 14
- adj_close: 57.14%
- volume: 57.14%
- num_trades_USDT: 64.29%
- close_BTC: 42.86%
- num_trades_BTC: 7.14%
- close_BNB: 35.71%
- num_trades_BNB: 42.86%
- close_XRP: 100.00%
- num_trades_XRP: 7.14%  
Average All: 46.03%  
Average Closes: 58.93%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1639.33791  
Start: 1639.33791, First week Forecast: 1606.15572, 1553.88411, 1485.93979, 1403.21782, 1307.14190, 1192.87834, 1066.44509  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 206.89016  
Next Day Forecast Difference to Real Value: 136.41402  
Next Day Difference in Standard Deviations: 0.10199  
Next Day Forecast:   DOWN -33.18219  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -261.81443  
First Week Difference in Standard Deviations: -0.19575  
First Week Forecast: DOWN -572.89282  
First Week Real:     DOWN -104.18823  
 
Two Week Forecast:   DOWN -1616.73481  
Two Week Real:       DOWN -104.46912  

### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.07434  
Start: 0.07434, First week Forecast: 0.07257, 0.07066, 0.06863, 0.06651, 0.06429, 0.06194, 0.05951  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: 0.00193  

Next Day Forecast Difference to Real Value: -0.00046  
Next Day Difference in Standard Deviations: -0.02085  
Next Day Forecast:   DOWN -0.00177  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: -0.00930  
First Week Difference in Standard Deviations: -0.42239  
First Week Forecast: DOWN -0.01484  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   DOWN -0.03520  
Two Week Real:       DOWN -0.00400  

### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.17249  
Start: 0.17249, First week Forecast: 0.17564, 0.18017, 0.18593, 0.19280, 0.20064, 0.20951, 0.21916  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.01921  

Next Day Forecast Difference to Real Value: -0.01436  
Next Day Difference in Standard Deviations: -0.32065  
Next Day Forecast:   UP   0.00315  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: 0.01076  
First Week Difference in Standard Deviations: 0.24031  
First Week Forecast: UP   0.04667  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.12495  
Two Week Real:       UP   0.02260  
 
### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00025  
Start: 0.00025, First week Forecast: 0.00025, 0.00026, 0.00026, 0.00026, 0.00027, 0.00028, 0.00028  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: 0.00001  

Next Day Forecast Difference to Real Value: -0.00000  
Next Day Difference in Standard Deviations: -0.00315  
Next Day Forecast:   UP   0.00000  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00010  
First Week Difference in Standard Deviations: -0.22893  
First Week Forecast: UP   0.00003  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00012  
Two Week Real:       UP   0.00011  

---
# Senti_01_02 | Stock_01_02 - CryptoCurrencies
### Predictions within 0.3 standard deviations of actual value:
[992, 527, 566, 987, 483, 861, 602, 982, 608] out of 1081
- adj_close: 91.77%
- volume: 48.75%
- num_trades_USDT: 52.36%
- close_BTC: 91.30%
- num_trades_BTC: 44.68%
- close_BNB: 79.65%
- num_trades_BNB: 55.69%
- close_XRP: 90.84%
- num_trades_XRP: 56.24%  
Average All: 67.92%  
Average Closes: 88.39%  

### First week Forecasts within 0.3 standard deviations of actual value:
[6, 5, 5, 5, 0, 2, 5, 7, 1] out of 7
- adj_close: 85.71%
- volume: 71.43%
- num_trades_USDT: 71.43%
- close_BTC: 71.43%
- num_trades_BTC: 0.00%
- close_BNB: 28.57%
- num_trades_BNB: 71.43%
- close_XRP: 100.00%
- num_trades_XRP: 14.29%  
Average All: 57.14%  
Average Closes: 71.43%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[13, 9, 6, 9, 2, 3, 8, 10, 1] out of 14
- adj_close: 92.86%
- volume: 64.29%
- num_trades_USDT: 42.86%
- close_BTC: 64.29%
- num_trades_BTC: 14.29%
- close_BNB: 21.43%
- num_trades_BNB: 57.14%
- close_XRP: 71.43%
- num_trades_XRP: 7.14%  
Average All: 48.41%  
Average Closes: 62.50%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1894.18662  
Start: 1894.18662, First week Forecast: 1848.15630, 1781.19559, 1697.68869, 1601.70230, 1498.33619, 1388.85953, 1281.50028  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 461.73887  

Next Day Forecast Difference to Real Value: 378.41460  
Next Day Difference in Standard Deviations: 0.28293  
Next Day Forecast:   DOWN -46.03032  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -46.75924  
First Week Difference in Standard Deviations: -0.03496  
First Week Forecast: DOWN -612.68634  
First Week Real:     DOWN -104.18823  

Two Week Forecast:   DOWN -783.02115  
Two Week Real:       DOWN -104.46912  

### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.07644  
Start: 0.07644, First week Forecast: 0.07604, 0.07568, 0.07535, 0.07507, 0.07484, 0.07466, 0.07456  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: 0.00403  

Next Day Forecast Difference to Real Value: 0.00302  
Next Day Difference in Standard Deviations: 0.13698  
Next Day Forecast:   DOWN -0.00039  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: 0.00575  
First Week Difference in Standard Deviations: 0.26131  
First Week Forecast: DOWN -0.00188  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   UP   0.00378  
Two Week Real:       DOWN -0.00400  

### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.16200  
Start: 0.16200, First week Forecast: 0.16608, 0.17178, 0.17873, 0.18667, 0.19531, 0.20415, 0.21256  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.02970  

Next Day Forecast Difference to Real Value: -0.02392  
Next Day Difference in Standard Deviations: -0.53411  
Next Day Forecast:   UP   0.00408  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: 0.00416  
First Week Difference in Standard Deviations: 0.09287  
First Week Forecast: UP   0.05056  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.07531  
Two Week Real:       UP   0.02260  

### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00023  
Start: 0.00023, First week Forecast: 0.00024, 0.00025, 0.00026, 0.00028, 0.00030, 0.00032, 0.00035  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: -0.00002  

Next Day Forecast Difference to Real Value: -0.00002  
Next Day Difference in Standard Deviations: -0.04460  
Next Day Forecast:   UP   0.00000  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00003  
First Week Difference in Standard Deviations: -0.07660  
First Week Forecast: UP   0.00012  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00035  
Two Week Real:       UP   0.00011  

---
# Senti_01_03 | Stock_01_03 - CryptoCurrency
### Predictions within 0.3 standard deviations of actual value:
[978, 526, 562, 1004, 481, 873, 626, 1003, 601] out of 1081
- adj_close: 90.47%
- volume: 48.66%
- num_trades_USDT: 51.99%
- close_BTC: 92.88%
- num_trades_BTC: 44.50%
- close_BNB: 80.76%
- num_trades_BNB: 57.91%
- close_XRP: 92.78%
- num_trades_XRP: 55.60%  
Average All: 68.39%  
Average Closes: 89.22%  

### First week Forecasts within 0.3 standard deviations of actual value:
[6, 5, 3, 7, 0, 5, 4, 7, 0] out of 7
- adj_close: 85.71%
- volume: 71.43%
- num_trades_USDT: 42.86%
- close_BTC: 100.00%
- num_trades_BTC: 0.00%
- close_BNB: 71.43%
- num_trades_BNB: 57.14%
- close_XRP: 100.00%
- num_trades_XRP: 0.00%  
Average All: 58.73%  
Average Closes: 89.29%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[6, 9, 3, 14, 0, 5, 5, 14, 1] out of 14
- adj_close: 42.86%
- volume: 64.29%
- num_trades_USDT: 21.43%
- close_BTC: 100.00%
- num_trades_BTC: 0.00%
- close_BNB: 35.71%
- num_trades_BNB: 35.71%
- close_XRP: 100.00%
- num_trades_XRP: 7.14%  
Average All: 45.24%  
Average Closes: 69.64%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1461.30112  
Start: 1461.30112, First week Forecast: 1408.69940, 1347.13186, 1272.35847, 1185.39865, 1088.57591, 981.60892, 865.23649  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 28.85337  

Next Day Forecast Difference to Real Value: -61.04230  
Next Day Difference in Standard Deviations: -0.04564  
Next Day Forecast:   DOWN -52.60172  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -463.02303  
First Week Difference in Standard Deviations: -0.34619  
First Week Forecast: DOWN -596.06463  
First Week Real:     DOWN -104.18823  

Two Week Forecast:   DOWN -1603.09279  
Two Week Real:       DOWN -104.46912  

### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.07163  
Start: 0.07163, First week Forecast: 0.07029, 0.06934, 0.06862, 0.06811, 0.06778, 0.06764, 0.06765  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: -0.00078  

Next Day Forecast Difference to Real Value: -0.00274  
Next Day Difference in Standard Deviations: -0.12425  
Next Day Forecast:   DOWN -0.00134  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: -0.00116  
First Week Difference in Standard Deviations: -0.05271  
First Week Forecast: DOWN -0.00399  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   DOWN -0.00054  
Two Week Real:       DOWN -0.00400  
 
### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.17546  
Start: 0.17546, First week Forecast: 0.17979, 0.18528, 0.19216, 0.20029, 0.20968, 0.22030, 0.23211  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.01624  

Next Day Forecast Difference to Real Value: -0.01021  
Next Day Difference in Standard Deviations: -0.22792  
Next Day Forecast:   UP   0.00433  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: 0.02371  
First Week Difference in Standard Deviations: 0.52927  
First Week Forecast: UP   0.05665  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.17078  
Two Week Real:       UP   0.02260  

### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00025  
Start: 0.00025, First week Forecast: 0.00026, 0.00026, 0.00027, 0.00027, 0.00028, 0.00029, 0.00029  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: 0.00000  

Next Day Forecast Difference to Real Value: -0.00000  
Next Day Difference in Standard Deviations: -0.00108  
Next Day Forecast:   UP   0.00001  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00009  
First Week Difference in Standard Deviations: -0.20173  
First Week Forecast: UP   0.00004  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00009  
Two Week Real:       UP   0.00011  

---
# Senti_01_04 | Stock_01_04 - Cryptomarkets
### Predictions within 0.3 standard deviations of actual value:
[995, 527, 562, 995, 504, 865, 628, 975, 605] out of 1081
- adj_close: 92.04%
- volume: 48.75%
- num_trades_USDT: 51.99%
- close_BTC: 92.04%
- num_trades_BTC: 46.62%
- close_BNB: 80.02%
- num_trades_BNB: 58.09%
- close_XRP: 90.19%
- num_trades_XRP: 55.97%  
Average All: 68.41%  
Average Closes: 88.58%  

### First week Forecasts within 0.3 standard deviations of actual value:
[7, 4, 4, 4, 0, 3, 5, 7, 0] out of 7
- adj_close: 100.00%
- volume: 57.14%
- num_trades_USDT: 57.14%
- close_BTC: 57.14%
- num_trades_BTC: 0.00%
- close_BNB: 42.86%
- num_trades_BNB: 71.43%
- close_XRP: 100.00%
- num_trades_XRP: 0.00%  
Average All: 53.97%  
Average Closes: 75.00%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[9, 8, 8, 11, 1, 8, 7, 14, 1] out of 14
- adj_close: 64.29%
- volume: 57.14%
- num_trades_USDT: 57.14%
- close_BTC: 78.57%
- num_trades_BTC: 7.14%
- close_BNB: 57.14%
- num_trades_BNB: 50.00%
- close_XRP: 100.00%
- num_trades_XRP: 7.14%  
Average All: 53.17%  
Average Closes: 75.00%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1769.29688  
Start: 1769.29688, First week Forecast: 1666.99564, 1556.21969, 1439.64059, 1314.57710, 1188.99225, 1073.03113, 974.61851  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 336.84912  

Next Day Forecast Difference to Real Value: 197.25394  
Next Day Difference in Standard Deviations: 0.14748  
Next Day Forecast:   DOWN -102.30123  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -353.64102  
First Week Difference in Standard Deviations: -0.26441  
First Week Forecast: DOWN -794.67837  
First Week Real:     DOWN -104.18823  

Two Week Forecast:   DOWN -600.90365  
Two Week Real:       DOWN -104.46912  

### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.08020  
Start: 0.08020, First week Forecast: 0.07976, 0.07878, 0.07739, 0.07578, 0.07402, 0.07223, 0.07056  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: 0.00778  

Next Day Forecast Difference to Real Value: 0.00673  
Next Day Difference in Standard Deviations: 0.30552  
Next Day Forecast:   DOWN -0.00044  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: 0.00175  
First Week Difference in Standard Deviations: 0.07944  
First Week Forecast: DOWN -0.00964  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   DOWN -0.00956  
Two Week Real:       DOWN -0.00400  

### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.16555  
Start: 0.16555, First week Forecast: 0.17121, 0.17744, 0.18400, 0.19081, 0.19750, 0.20348, 0.20824  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.02615  

Next Day Forecast Difference to Real Value: -0.01879  
Next Day Difference in Standard Deviations: -0.41946  
Next Day Forecast:   UP   0.00566  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: -0.00016  
First Week Difference in Standard Deviations: -0.00357  
First Week Forecast: UP   0.04269  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.01596  
Two Week Real:       UP   0.02260  

### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00021  
Start: 0.00021, First week Forecast: 0.00020, 0.00020, 0.00021, 0.00022, 0.00023, 0.00024, 0.00025  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: -0.00004  

Next Day Forecast Difference to Real Value: -0.00005  
Next Day Difference in Standard Deviations: -0.12133  
Next Day Forecast:   DOWN -0.00000  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00013  
First Week Difference in Standard Deviations: -0.29090  
First Week Forecast: UP   0.00005  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00011  
Two Week Real:       UP   0.00011  

---
# Senti_01_05 | Stock_01_05 - eth
### Predictions within 0.3 standard deviations of actual value:
[974, 539, 563, 1016, 505, 857, 587, 996, 612] out of 1081
- adj_close: 90.10%
- volume: 49.86%
- num_trades_USDT: 52.08%
- close_BTC: 93.99%
- num_trades_BTC: 46.72%
- close_BNB: 79.28%
- num_trades_BNB: 54.30%
- close_XRP: 92.14%
- num_trades_XRP: 56.61%  
Average All: 68.34%  
Average Closes: 88.88%  

### First week Forecasts within 0.3 standard deviations of actual value:
[7, 5, 4, 7, 1, 2, 6, 5, 0] out of 7
- adj_close: 100.00%
- volume: 71.43%
- num_trades_USDT: 57.14%
- close_BTC: 100.00%
- num_trades_BTC: 14.29%
- close_BNB: 28.57%
- num_trades_BNB: 85.71%
- close_XRP: 71.43%
- num_trades_XRP: 0.00%  
Average All: 58.73%  
Average Closes: 75.00%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[8, 7, 4, 14, 1, 3, 6, 10, 0] out of 14
- adj_close: 57.14%
- volume: 50.00%
- num_trades_USDT: 28.57%
- close_BTC: 100.00%
- num_trades_BTC: 7.14%
- close_BNB: 21.43%
- num_trades_BNB: 42.86%
- close_XRP: 71.43%
- num_trades_XRP: 0.00%  
Average All: 42.06%  
Average Closes: 62.50%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1732.19483  
Start: 1732.19483, First week Forecast: 1685.66472, 1622.01380, 1544.73880, 1455.60824, 1355.74613, 1247.21538, 1132.53148  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 299.74707  

Next Day Forecast Difference to Real Value: 215.92302  
Next Day Difference in Standard Deviations: 0.16144  
Next Day Forecast:   DOWN -46.53011  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -195.72804  
First Week Difference in Standard Deviations: -0.14634  
First Week Forecast: DOWN -599.66335  
First Week Real:     DOWN -104.18823  

Two Week Forecast:   DOWN -1416.68356  
Two Week Real:       DOWN -104.46912  

### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.07723  
Start: 0.07723, First week Forecast: 0.07620, 0.07521, 0.07421, 0.07319, 0.07218, 0.07116, 0.07011  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: 0.00482  

Next Day Forecast Difference to Real Value: 0.00317  
Next Day Difference in Standard Deviations: 0.14387  
Next Day Forecast:   DOWN -0.00103  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: 0.00130  
First Week Difference in Standard Deviations: 0.05920  
First Week Forecast: DOWN -0.00712  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   DOWN -0.01328  
Two Week Real:       DOWN -0.00400  

### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.15783  
Start: 0.15783, First week Forecast: 0.16070, 0.16522, 0.17117, 0.17842, 0.18682, 0.19619, 0.20623  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.03387  

Next Day Forecast Difference to Real Value: -0.02930  
Next Day Difference in Standard Deviations: -0.65418  
Next Day Forecast:   UP   0.00286  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: -0.00217  
First Week Difference in Standard Deviations: -0.04837  
First Week Forecast: UP   0.04840  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.12167  
Two Week Real:       UP   0.02260  

### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00021  
Start: 0.00021, First week Forecast: 0.00021, 0.00021, 0.00021, 0.00022, 0.00022, 0.00023, 0.00023  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: -0.00004  

Next Day Forecast Difference to Real Value: -0.00004  
Next Day Difference in Standard Deviations: -0.10095  
Next Day Forecast:   DOWN -0.00000  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00015  
First Week Difference in Standard Deviations: -0.34177  
First Week Forecast: UP   0.00002  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00007  
Two Week Real:       UP   0.00011  

---
# Senti_01_06 | Stock_01_06 - ethfinance
### Predictions within 0.3 standard deviations of actual value:
[982, 526, 572, 1002, 493, 918, 604, 986, 612] out of 1081
- adj_close: 90.84%
- volume: 48.66%
- num_trades_USDT: 52.91%
- close_BTC: 92.69%
- num_trades_BTC: 45.61%
- close_BNB: 84.92%
- num_trades_BNB: 55.87%
- close_XRP: 91.21%
- num_trades_XRP: 56.61%  
Average All: 68.81%  
Average Closes: 89.92%  

### First week Forecasts within 0.3 standard deviations of actual value:
[6, 2, 3, 6, 1, 5, 4, 7, 0] out of 7
- adj_close: 85.71%
- volume: 28.57%
- num_trades_USDT: 42.86%
- close_BTC: 85.71%
- num_trades_BTC: 14.29%
- close_BNB: 71.43%
- num_trades_BNB: 57.14%
- close_XRP: 100.00%
- num_trades_XRP: 0.00%  
Average All: 53.97%  
Average Closes: 85.71%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[6, 5, 3, 6, 1, 5, 5, 14, 3] out of 14
- adj_close: 42.86%
- volume: 35.71%
- num_trades_USDT: 21.43%
- close_BTC: 42.86%
- num_trades_BTC: 7.14%
- close_BNB: 35.71%
- num_trades_BNB: 35.71%
- close_XRP: 100.00%
- num_trades_XRP: 21.43%  
Average All: 38.10%  
Average Closes: 55.36%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1814.99232  
Start: 1814.99232, First week Forecast: 1799.06516, 1751.43977, 1674.82149, 1568.70030, 1435.39398, 1276.50784, 1093.56296  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 382.54457  

Next Day Forecast Difference to Real Value: 329.32347  
Next Day Difference in Standard Deviations: 0.24623  
Next Day Forecast:   DOWN -15.92716  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -234.69656  
First Week Difference in Standard Deviations: -0.17548  
First Week Forecast: DOWN -721.42937  
First Week Real:     DOWN -104.18823  

Two Week Forecast:   DOWN -2625.98603  
Two Week Real:       DOWN -104.46912  

### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.07366  
Start: 0.07366, First week Forecast: 0.07260, 0.07124, 0.06958, 0.06772, 0.06568, 0.06351, 0.06119  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: 0.00125  

Next Day Forecast Difference to Real Value: -0.00043  
Next Day Difference in Standard Deviations: -0.01954  
Next Day Forecast:   DOWN -0.00107  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: -0.00762  
First Week Difference in Standard Deviations: -0.34600  
First Week Forecast: DOWN -0.01248  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   DOWN -0.03202  
Two Week Real:       DOWN -0.00400  

### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.17281  
Start: 0.17281, First week Forecast: 0.17668, 0.18242, 0.18980, 0.19874, 0.20916, 0.22092, 0.23387  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.01889  

Next Day Forecast Difference to Real Value: -0.01332  
Next Day Difference in Standard Deviations: -0.29739  
Next Day Forecast:   UP   0.00387  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: 0.02547  
First Week Difference in Standard Deviations: 0.56867  
First Week Forecast: UP   0.06106  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.18212  
Two Week Real:       UP   0.02260  

### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00024  
Start: 0.00024, First week Forecast: 0.00024, 0.00024, 0.00024, 0.00024, 0.00024, 0.00025, 0.00025  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: -0.00001  

Next Day Forecast Difference to Real Value: -0.00002  
Next Day Difference in Standard Deviations: -0.04075  
Next Day Forecast:   DOWN -0.00000  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00013  
First Week Difference in Standard Deviations: -0.29964  
First Week Forecast: UP   0.00001  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00006  
Two Week Real:       UP   0.00011  

---
# Senti_01_07 | Stock_01_07 - ethtrader
### Predictions within 0.3 standard deviations of actual value:
[984, 538, 573, 998, 495, 852, 589, 974, 609] out of 1081
- adj_close: 91.03%
- volume: 49.77%
- num_trades_USDT: 53.01%
- close_BTC: 92.32%
- num_trades_BTC: 45.79%
- close_BNB: 78.82%
- num_trades_BNB: 54.49%
- close_XRP: 90.10%
- num_trades_XRP: 56.34%  
Average All: 67.96%  
Average Closes: 88.07%  

### First week Forecasts within 0.3 standard deviations of actual value:
[7, 5, 5, 7, 0, 1, 4, 7, 0]
- adj_close: 100.00%
- volume: 71.43%
- num_trades_USDT: 71.43%
- close_BTC: 100.00%
- num_trades_BTC: 0.00%
- close_BNB: 14.29%
- num_trades_BNB: 57.14%
- close_XRP: 100.00%
- num_trades_XRP: 0.00%  
Average All: 57.14%  
Average Closes: 78.57%  

### Two week Forecasts within 0.3 standard deviations of actual value:
[14, 8, 10, 8, 2, 6, 6, 14, 1]
- adj_close: 100.00%
- volume: 57.14%
- num_trades_USDT: 71.43%
- close_BTC: 57.14%
- num_trades_BTC: 14.29%
- close_BNB: 42.86%
- num_trades_BNB: 42.86%
- close_XRP: 100.00%
- num_trades_XRP: 7.14%  
Average All: 54.76%  
Average Closes: 75.00%  

### Forecast Results vs Real Values in adj_close ETH-USD:
Last prediction (in training): 1731.09128  
Start: 1731.09128, First week Forecast: 1672.53621, 1602.89104, 1526.54346, 1447.37929, 1370.18765, 1297.88576, 1232.09844  
Start: 1432.44775, First week Real:     1469.74170, 1335.32910, 1377.54138, 1324.38818, 1252.60779, 1327.68018, 1328.25952  
Start Difference: 298.64353  

Next Day Forecast Difference to Real Value: 202.79452  
Next Day Difference in Standard Deviations: 0.15163  
Next Day Forecast:   DOWN -58.55507  
Next Day Real:       UP   37.29394  

First Week Forecast Difference to Real Value: -96.16108  
First Week Difference in Standard Deviations: -0.07190  
First Week Forecast: DOWN -498.99284  
First Week Real:     DOWN -104.18823  

Two Week Forecast:   DOWN -483.40665  
Two Week Real:       DOWN -104.46912  

#### Forecast Results vs Real Values in close_BTC ETH-BTC:
Last prediction (in training): 0.07572  
Start: 0.07572, First week Forecast: 0.07479, 0.07357, 0.07210, 0.07043, 0.06861, 0.06673, 0.06490  
Start: 0.07241, First week Real:     0.07303, 0.06872, 0.07043, 0.07010, 0.06749, 0.06836, 0.06881  
Start Difference: 0.00331  

Next Day Forecast Difference to Real Value: 0.00176  
Next Day Difference in Standard Deviations: 0.07993  
Next Day Forecast:   DOWN -0.00093  
Next Day Real:       UP   0.00061  

First Week Forecast Difference to Real Value: -0.00391  
First Week Difference in Standard Deviations: -0.17759  
First Week Forecast: DOWN -0.01082  
First Week Real:     DOWN -0.00361  

Two Week Forecast:   DOWN -0.01946  
Two Week Real:       DOWN -0.00400  

#### Forecast Results vs Real Values in close_BNB BNB-ETH:
Last prediction (in training): 0.15798  
Start: 0.15798, First week Forecast: 0.16184, 0.16688, 0.17271, 0.17896, 0.18521, 0.19103, 0.19624  
Start: 0.19170, First week Real:     0.19000, 0.19950, 0.19770, 0.20120, 0.21190, 0.20750, 0.20840  
Start Difference: -0.03372  

Next Day Forecast Difference to Real Value: -0.02816  
Next Day Difference in Standard Deviations: -0.62858  
Next Day Forecast:   UP   0.00387  
Next Day Real:       DOWN -0.00170  

First Week Forecast Difference to Real Value: -0.01216  
First Week Difference in Standard Deviations: -0.27149  
First Week Forecast: UP   0.03826  
First Week Real:     UP   0.01670  

Two Week Forecast:   UP   0.03388  
Two Week Real:       UP   0.02260  

### Forecast Results vs Real Values in close_XRP XRP-ETH:
Last prediction (in training): 0.00026  
Start: 0.00026, First week Forecast: 0.00025, 0.00025, 0.00025, 0.00026, 0.00027, 0.00029, 0.00030  
Start: 0.00025, First week Real:     0.00026, 0.00027, 0.00028, 0.00031, 0.00032, 0.00037, 0.00038  
Start Difference: 0.00001  

Next Day Forecast Difference to Real Value: -0.00000  
Next Day Difference in Standard Deviations: -0.00982  
Next Day Forecast:   DOWN -0.00000  
Next Day Real:       UP   0.00001  

First Week Forecast Difference to Real Value: -0.00008  
First Week Difference in Standard Deviations: -0.18422  
First Week Forecast: UP   0.00005  
First Week Real:     UP   0.00013  

Two Week Forecast:   UP   0.00020  
Two Week Real:       UP   0.00011  
