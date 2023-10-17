def bubble_sort(list):
    n = len(list)  # Obtenemos la longitud de la lista.
    for i in range(n):  # Recorremos la lista n veces.
        for j in range(0, n-i-1):  # Recorremos la lista desde el principio hasta n-i-1 que es el índice del último elemento no ordenado en cada iteración del bucle.
            if list[j] > list[j+1]:  # Comparamos dos elementos adyacentes.
                list[j], list[j+1] = list[j+1], list[j]  # Intercambiamos los elementos si están en el orden incorrecto.
    return list  # Devolvemos la lista ordenada.

def selection_sort(list):
    n = len(list)  # Obtenemos la longitud de la lista.
    for i in range(n):  # Recorremos la lista n veces.
        min_index = i  # Suponemos que el elemento actual es el mínimo.
        for j in range(i+1, n):  # Recorremos el resto de la lista.
            if list[j] < list[min_index]:  # Si encontramos un elemento más pequeño, actualizamos min_index.
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]  # Intercambiamos el elemento actual con el mínimo.
    return list  # Devolvemos la lista ordenada.

def insertion_sort(list):
    for i in range(1, len(list)):  # Empezamos desde el segundo elemento.
        key = list[i]  # Tomamos el elemento actual como "clave".
        j = i - 1  # Comenzamos a comparar con el elemento anterior.
        while j >= 0 and key < list[j]:  # Mientras la clave sea menor y no hayamos llegado al principio.
            list[j + 1] = list[j]  # Desplazamos los elementos mayores hacia la derecha.
            j -= 1
        list[j + 1] = key  # Insertamos la clave en la posición correcta.
    return list  # Devolvemos la lista ordenada.

def merge_sort(list):
    if len(list) <= 1:  # Si la lista tiene 1 o 0 elementos, ya está ordenada.
        return list

    mid = len(list) // 2  # Encontramos el punto medio de la lista.
    left = list[:mid]  # Dividimos la lista en dos mitades.
    right = list[mid:]

    left = merge_sort(left)  # Llamamos recursivamente a merge_sort en ambas mitades.
    right = merge_sort(right)

    return merge(left, right)  # Combinamos las dos mitades ordenadas utilizando la función merge.

def merge(left, right):
    result = []  # Creamos una lista vacía para combinar los elementos.
    i = j = 0  # Índices para recorrer las dos listas.

    while i < len(left) and j < len(right):  # Mientras haya elementos en ambas listas.
        if left[i] < right[j]:  # Comparamos los elementos de ambas listas.
            result.append(left[i])  # Agregamos el elemento más pequeño a result.
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # Agregamos los elementos restantes (si los hay) de ambas listas.
    result.extend(right[j:])
    return result  # Devolvemos la lista combinada y ordenada.

# Búsqueda Lineal
def linear_search(list, element_searched):
    index = -1  # Suponemos que el elemento no está en la lista.
    for i in range(len(list)):  # Recorremos la lista.
        if list[i] == element_searched:  # Comparamos el elemento actual con el buscado.
            index = i  # Si encontramos una coincidencia, actualizamos el índice.
            break  # Salimos del bucle una vez que se ha encontrado la primera coincidencia.
    return index  # Devolvemos el índice del elemento buscado o -1 si no se encontró.

# Búsqueda Binaria
def binary_search(list, element_searched):
    left, right = 0, len(list) - 1  # Definimos los límites izquierdo y derecho de la búsqueda.
    while left <= right:  # Mientras el rango de búsqueda sea válido.
        half = (left + right) // 2  # Encontramos el punto medio.
        if list[half] == element_searched:  # Comparamos el elemento del punto medio con el buscado.
            return half  # Si son iguales, devolvemos el índice del elemento encontrado.
        elif list[half] < element_searched:  # Si el elemento del punto medio es menor, ajustamos el límite izquierdo.
            left = half + 1
        else:  # Si el elemento del punto medio es mayor, ajustamos el límite derecho.
            right = half - 1
    return -1  # Devolvemos -1 si el elemento no se encuentra en la lista.

