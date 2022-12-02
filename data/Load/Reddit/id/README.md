# API Reference 

## subreddits_id.py

```
get_data(**kargs)
````
| Parameter | Type     |
| :-------- | :------- |  
| `kargs` | `diccionario` |

Realiza una llamada a la api de pushshift utilizando los elementos del diccionario en donde devuelve un json con los identificadores de las publicaciones.

```
get_post_id(subreddits, date_range_list)
````
| Parameter | Type     | Description |
| :-------- | :------- | :------- | 
| `subreddits` | `string list` | nombres de subreddits |
| `date_range_list` | `int list` | marca de tiempo unix |

Utiliza la función de get_data para obtener un dataframe que contiene el nombre del subreddit y el identificador de un post.

```
get_date_range(start, end)
````
| Parameter | Type     | Description |
| :-------- | :------- | :------- |   
| `start` | `string` | fecha y/m/d |
| `end` | `string` | fecha y/m/d |

Devuelve un lista que contiene todas las marcas de tiempo unix dentro de start y end.
