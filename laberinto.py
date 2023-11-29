
# Crear una función que hace que se cree el laberinto.
# Pone 'X' en las coordenadas correspondientes al muro (indicacas más abajo).
# También pone espacios ('') en las coordenadas que no corresponden al muro.

def crear_laberinto(filas, columnas, coordenadas_muro):

    # En este comando se asigna una 'X' o un '' a las coordenadas correspodientes.
    laberinto = [['X' if (fila, col) in coordenadas_muro else ' ' for col in range(columnas)] for fila in range(filas)]

    laberinto[4][4] = 'S'  # 'S' (de Salida) al final
    laberinto[0][0] = 'E'  # 'E' (de Entrada) al principio

    return laberinto


# Función que hace que el laberinto aparezca como tal en el terminal al ejecutar el programa.
def imprimir_laberinto(laberinto):

    for fila in laberinto:

        # la función "join" hace que se puedan concatenar los elementos de la lista "fila" para que así se vea correctamente en formato de laberinto.
        print(" ".join(fila))



# Creamos una función para hacer el print de la solución con los movimientos que hay que realizar para salir del laberinto
def solucion_laberinto(laberinto):

    # Fila y columnas iniciales
    fila = 1
    columna = 0

    # 'n' son las posiciones que tiene que recorrer el bucle while y corresponde con el tamaño de la lista que constituye al laberinto
    n = len(laberinto)

    # Lista de movimientos
    movimientos = ['Abajo']

    # fila y columna n-1 representa la ultima posición del laberinto, la correspondiente con la salida
    while not (fila == n-1 and columna == n-1):

        # Cada 'if' comprueba distitas condiciones:
        # - Que la acción anterior no sea lo contrario (porque no tendría sentido hacer una 'abajo' después de un 'arriba')
        # - Que la seguiente posición hacia ese sentido exista en el laberinto
        # - Que la seguiente posición hacia ese sentido no sea un muro
        # En caso de que las tres consiciones se cumplan, se avanza hacia dicho sentido y se añade la dirección del movimiento a la lista 'movimientos'

        if movimientos[-1] != 'Arriba' and (fila + 1) < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')

        elif movimientos[-1] != 'Abajo' and (fila - 1) > 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')

        elif movimientos[-1] != 'Izquierda' and (columna + 1) < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')

        elif movimientos[-1] != 'Derecha' and (columna - 1) > 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')

        else:
            # No hay salida en caso de que ninguna de las condiciones sea cierta
            return [("No hay salida",)]


    # La solución es el print de la lista 'movimientos'
    print('Solución:', movimientos)




# "if __name__ == "__main__"" hace que el código y las funciones dentro de dicha función se ejectuten si el script es ejecutado directamente.
if __name__ == "__main__":
    
    # Estas variables hacen que se pueda adaptar el tamaño y forma del laberinto a caulquier medida. 
    # Se puede editar el número de filas, columnas y las coordenadas del muro.
    filas = 5
    columnas = 5
    coordenadas_muro = {(0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)}

    # Aquí se ejecutan las funciones definidas anteriormente para que el código saque el resultado esperado del laberinto creado.
    laberinto = crear_laberinto(filas, columnas, coordenadas_muro)
    imprimir_laberinto(laberinto)

    # Añadiendo la función para el print de la solución del laberinto al script
    solucion_laberinto(laberinto)