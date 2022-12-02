# API REFERENCE

### model_short_forecast.ipynb

| `class SentientAnalizer` |
| :- |
| Modelo de análisis de sentimiento con vocabulary embedding, LSTM layers y Linear layers. |

| Variables |
| :- |
| input_size: int|
| hidden_size: int |
| output_size: int |
| vocab_size: int |
| embedding_dim: int |

| Metodos |
| :-: |
| Funcion | Parametros | Descripción |
|forward(x, hidden) | [x: torch tensor] - [hidden: object]  - [stock_news: torch tensor] | Recibe el toch tensor y el hidden layer para generar un tensor output. |  
|init_hidden(batch_size) | [batch_size: int] | Recibe el toch tensor y el hidden layer para generar un tensor output. |  

| `class StockPredictor` |
| :- |
| Modelo de predicción de precios con capa de atención para entender el contexto de las variables, capas LSTM y capas lineales. Toma 9 variables y la salida de sentimiento como entradas, y genera las 9 variables para el siguiente paso (día siguiente). |

| Variables |
| :- |
| input_size_stock: int|
| input_size_sentiment: int |
| hidden_size: int |
| num_layers: int |
| max_length: int |

| Metodos |
| :-: |
| Funcion | Parametros | Descripción |
|forward(x, hidden) | [x: torch tensor] - [hidden: object]  - [stock_news: torch tensor] | Recibe el toch tensor y el hidden layer para generar un tensor output. |  
|init_hidden(batch_size) | [batch_size: int] | Recibe el toch tensor y el hidden layer para generar un tensor output. |  

| `class Dataset` |
| :- |
| Genera un conjunto de datos con variables de entrada. Los datos se dividen en 1089 días para el entrenamiento y 7 días para la prueba. Las muestras de prueba son los últimos 7 días del conjunto de datos.  |

| Variables |
| :- |
| data_stock: torch tensor (floats)|
| notice: torch tensor (long) |
| target: torch tensor |

| Metodos |
| :-: |
| Funcion | Parametros | Descripción |
|def __len__() | | Regresa el tamaño de los datos |  
|def __getitem__(idx) | [idx:int] | Regresa un elemento de un tensor a partir del idx. |  
