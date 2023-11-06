# Función para verificar si una cadena contiene solo las letras A, T, C o G
def valid_string(string):
    # Definimos una cadena de caracteres válidos (A, T, C, G)
    valid_characters = 'ATCG'
    # Recorremos cada carácter en la cadena
    for character in string:
        # Comprobamos si el carácter actual no está en la lista de caracteres válidos
        if character not in valid_characters:
            # Si encontramos un carácter no válido, retornamos False
            return False
    
    # Si no se encontraron caracteres inválidos, retornamos True
    return True

# Función para ingresar una secuencia de ADN.
def enter_sequence():
    while True:
        # Solicita al usuario que ingrese una secuencia de ADN y convierte la entrada a mayúsculas
        sequence = input("Ingrese una fila de ADN (solo letras A, T, C, G y no más de 6 caracteres): ").upper()
        
        # Comprueba si la longitud de la secuencia no es igual a 6 caracteres
        if len(sequence) != 6:
            print("La fila debe tener exactamente 6 caracteres.")
        # Comprueba si la secuencia no contiene caracteres inválidos
        elif not valid_string(sequence):
            print("La fila solo debe contener las letras A, T, C o G.")
        else:
            # Si la secuencia es válida, retorna la secuencia
            return sequence


# Función para imprimir la matriz de ADN en formato 6x6
def print_matrix(dna):
    # Recorre las filas de la matriz
    for row in range(6):
        # Recorre las columnas de la matriz.
        for column in range(6):
            print(dna[row][column], end=" ")  # Imprime el elemento en la posición (fila, columna).
            # El argumento end=" " se utiliza para indicar que, después de imprimir el elemento, se debe agregar un espacio en lugar de un salto de línea.
        print()  # Agrega un salto de línea después de imprimir una fila completa


def is_mutant(dna):
    # Inicializamos los contadores de secuencias.
    horizontal_sequences = 0
    vertical_sequences = 0
    oblique_sequences = 0

    # Búsqueda de secuencias horizontales

    # Itera a través de las filas de la matriz de ADN
    for row in range(len(dna)):
        # Itera a través de las columnas, con un límite de 3 columnas antes del final,
        # esto se hace a propósito para evitar que se intente acceder a índices que están fuera del rango válido.
        for column in range(len(dna[0]) - 3):
            # Comprueba si hay una secuencia de cuatro letras iguales en la misma fila.
            if dna[row][column] == dna[row][column + 1] == dna[row][column + 2] == dna[row][column + 3]:
                # Incrementa el contador de secuencias horizontales si se encuentra una secuencia de 4 letras iguales.
                horizontal_sequences += 1

    # Búsqueda de secuencias verticales

    # Itera a través de las columnas de la matriz de ADN
    for column in range(len(dna[0])):
        # Itera a través de las filas, con un límite de 3 filas antes del final,
        # esto se hace a propósito para evitar que se intente acceder a índices que están fuera del rango válido.
        for row in range(len(dna) - 3):
            # Comprueba si hay una secuencia de cuatro letras iguales en la misma columna.
            if dna[row][column] == dna[row + 1][column] == dna[row + 2][column] == dna[row + 3][column]:
                # Incrementa el contador de secuencias verticales si se encuentra una secuencia de 4 letras iguales.
                vertical_sequences += 1

    # Búsqueda de secuencias oblicuas (izquierda a derecha).

    # Itera a través de las filas, con un límite de 3 filas antes del final.
    for row in range(len(dna) - 3):
        # Itera a través de las columnas, con un límite de 3 columnas antes del final.
        for column in range(len(dna[0]) - 3):
            # Comprueba si hay una secuencia de cuatro letras iguales en diagonal (izquierda a derecha).
            if dna[row][column] == dna[row + 1][column + 1] == dna[row + 2][column + 2] == dna[row + 3][column + 3]:
                # Incrementa el contador de secuencias diagonales si se encuentra una secuencia de 4 letras iguales.
                oblique_sequences += 1

    # Búsqueda de secuencias oblicuas (derecha a izquierda).

    # Itera a través de las filas, con un límite de 3 filas antes del final
    for row in range(len(dna) - 3):
        # Itera a través de las columnas, comenzando desde la columna 3 y yendo hacia atrás.
        for column in range(3, len(dna[0])):
            # Comprueba si hay una secuencia de cuatro letras iguales en diagonal (derecha a izquierda).
            if dna[row][column] == dna[row + 1][column - 1] == dna[row + 2][column - 2] == dna[row + 3][column - 3]:
                # Incrementa el contador de secuencias diagonales si se encuentra una secuencia de 4 letras iguales.
                oblique_sequences += 1
    
    # Suma el total de secuencias encontradas en todas las direcciones.
    sequences = horizontal_sequences + vertical_sequences + oblique_sequences
    
    # Comprobar si se encontraron al menos dos secuencias de 4 letras iguales.
    if sequences >=2:
        return True  # Es un mutante
    else:
        return False  # No es un mutante






