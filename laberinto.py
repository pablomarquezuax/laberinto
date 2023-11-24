
# Crear una función que hace que se cree el laberinto.
# Pone 'X' en las coordenadas correspondientes al muro (indicacas más abajo).
# También pone espacios ('') en las coordenadas que no corresponden al muro.

def crear_laberinto(filas, columnas, coordenadas_muro):

    # En este comando se asigna una 'X' o un '' a las coordenadas correspodientes.
    laberinto = [['X' if (fila, col) in coordenadas_muro else ' ' for col in range(columnas)] for fila in range(filas)]

    laberinto[4][4] = 'S'  # 'S' (de Start) al principio
    laberinto[0][0] = 'E'  # 'E' (de End) al final

    return laberinto


# Función que hace que el laberinto aparezca como tal en el terminal al ejecutar el programa.
def imprimir_laberinto(laberinto):

    for fila in laberinto:

        # la función "join" hace que se puedan concatenar los elementos de la lista "fila" para que así se vea correctamente en formato de laberinto.
        print(" ".join(fila))


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