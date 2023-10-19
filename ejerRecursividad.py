"""1. Escribir una función que simule el siguiente experimento: Se tiene una rata en una 
jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma 
probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 
minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. 
La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero 
quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
La función debe devolver el tiempo que tarda la rata en salir de la jaula."""

import random

def time_output():
    # Generar un número aleatorio entre 1 y 3 que representa el camino elegido por la rata
    way = random.randint(1, 3)
    
    # Verificar el camino elegido por la rata
    if way == 1:
        # Si el camino es 1, la rata tarda 3 minutos y se llama recursivamente a la función
        # Esto simula que la rata regresa a la jaula y elige nuevamente un camino
        return 3 + time_output()
    elif way == 2:
        # Si el camino es 2, la rata tarda 5 minutos y se llama recursivamente a la función
        # Nuevamente, esto simula que la rata regresa a la jaula y elige un camino
        return 5 + time_output()
    else:
        # Si el camino es 3, la rata tarda 7 minutos y ha salido de la jaula
        # La recursión se detiene aquí
        return 7

# Llamar a la función 'tiempo_salida' para simular el tiempo que la rata tarda en salir
total_time = time_output()

# Imprimir el resultado que indica el tiempo que la rata tardó en salir de la jaula
print(f"La rata tardo {total_time} minutos en salir de la jaula.")


    
"""2. Escribir una consigna apropiada para la siguiente función. Asumir que n es un número 
entero.
def f(n):
    s = str(n)
    if len(s) <= 1:
    return s
    return s[-1] + f(int(s[:-1]))
"""

def f(n):
    # Convertir el número entero 'n' en una cadena de caracteres (string) y asignarlo a 's'
    s = str(n)
    
    # Verificar si la longitud de 's' es menor o igual a 1, lo que significa que 'n' es un número de una sola cifra
    if len(s) <= 1:
        # En este caso, simplemente devolvemos 's' como resultado
        return s
    
    # Si 'n' tiene más de una cifra, concatenamos el último dígito de 's' con la llamada recursiva de 'f'
    # La llamada recursiva se realiza con 'int(s[:-1])', lo que elimina el último dígito y lo convierte nuevamente en un entero
    return s[-1] + f(int(s[:-1]))


result = f(12345)
# Imprimir el resultado, que será la cadena resultante después de realizar la operación descrita en la función
print(result)  # Debe imprimir "54321"
