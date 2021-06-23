# Lab9: Similarity-based search

## P1. Threshold search

Complexity: `O(n)`

|PR|Q15|Q82|Q121|
|---|---|---|---|
|r1=2|1|0.68|0.46|
|r2=6|0.33|0.33|0.33|
|r3=9|0.33|0.33|0.33|

## P2. K nearest neighbors search

Complexity: `O(n log n)`
|PR|Q15|Q82|Q121|
|---|---|---|---|
|r1=2|1|1|1|
|r1=4|1|1|1|
|r1=8|1|1|0.9|
|r1=16|1|1|0.6|
|r1=32|1|1|0.5|

¿Cuál de los dos métodos de búsqueda usted usaría en un ambiente real de recuperación de la información?
- La busqueda de K Nearest neighbors es mucho mejor a la hora de obneter datos relevantes a mi busqueda, pero cuando se trata de imagenes uno quiere traer las mas parecidas asi misma por lo que si utilizamos esta busqueda pueda que imagen k este muy alejada y ya no tiene similitud con la original por lo que en estas situaciones una busqueda por rango seria mas favorable.
