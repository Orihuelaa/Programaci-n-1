# Elaborar una función que realice cada ordenamiento y búsqueda vistos en la presentación.

# TIPOS DE ORDENAMIENTO:

import funcionesOyB

list = [64, 34, 25, 12, 22, 11, 90]

sorted_list = funcionesOyB.bubble_sort(list)
print("Ordenamiento de Burbuja:", sorted_list)

sorted_list2 = funcionesOyB.selection_sort(list)
print("Orden de Selección:", sorted_list2)

sorted_list3 = funcionesOyB.insertion_sort(list)
print("Tipo de Inserción:", sorted_list3)

sorted_list4 = funcionesOyB.merge_sort(list)
print("Combinar Ordenamiento:", sorted_list4)


# TIPOS DE BUSQUEDA:

list2 = [5, 12, 34, 7, 2, 19, 45, 8]

search_element_linear = 7

binary_searched_element = 19

# Realizar la búsqueda lineal:
linear_index = funcionesOyB.linear_search(list2, search_element_linear)
if linear_index != -1: # Comprueba si se ha encontrado el elemento en la lista
    print(f"Elemento {search_element_linear} encontrado en el índice {linear_index}.")
else:
    print(f"Elemento {search_element_linear} no encontrado en la lista.")

# Realizar la búsqueda binaria:
binary_index = funcionesOyB.binary_search(list2, binary_searched_element)
if binary_index != -1: # Comprueba si se ha encontrado el elemento en la lista
    print(f"Elemento {binary_searched_element} encontrado en el índice {binary_index}.")
else:
    print(f"Elemento {binary_searched_element} no encontrado en la lista.")
