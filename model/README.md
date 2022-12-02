# API REFERENCE

### NOMBRE DE COIDGO

| class SentientAnalizer |
| :---------- |
| Modelo de análisis de sentimiento con vocabulary embedding, LSTM layers y Linear layers. |
| *** Variables *** |


```
  get_top3_comment(reddit, submission_id)
```
| Parameter | Type     |
| :-------- | :------- | 
| `reddit`      | `object` | 
| `sumbission_id`      | `string` |

Devuelve los primeros tres comentarios con el mayor número de “upvotes” o “me gusta” utilizando la instancia de la clase Reddit y el número de submission Id.