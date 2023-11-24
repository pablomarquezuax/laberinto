# Laberinto

## Tarea 1

Para poder ver este repositorio en línea, puedes hacerlo a través de este enlace: https://github.com/pablomarquezuax/laberinto.git 

### Instrucciones de la tarea:

La primera tarea consiste en **construir un laberinto como el de la siguiente figura**.

![Foto del laberinto que hay que crear](https://aprendeconalf.es/docencia/python/retos/img/laberinto.png)

El laberinto se representará como una una lista de listas, donde cada lista es una fila del laberinto y cada casilla se representará con un espacio ' ' si hay paso o con la letra ‘X’ si hay un muro, tal y como se muestra a continuación:

laberinto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]

El laberinto se debe crear a partir de una tupla con las coordenadas de las casillas donde hay muro, como la siguiente:

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))