"""Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.
Te ha contratado a ti para que desarrolles un programa que detecte si un humano es mutante basándose
en su secuencia de ADN.
Para eso te ha pedido crear un programa con un método o función booleana, llamada is_mutant(dna),
que recibe como parámetro un arreglo de Strings que representan cada fila de una matriz 6x6 con la
secuencia de ADN.
Las letras de los Strings solo pueden ser: A,T,C,G; las cuales representan cada base nitrogenada del ADN.
Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras iguales, estas
pueden aparecer de forma oblicua, horizontal o vertical.

En el caso de la matriz de la derecha,
adn = [‘ATGCGA’,’CAGTGC’,’TTATGT’,’AGAAGG’,’CCCCTA’,’TCACTG’]
la función devolverá True.
Desarrolla el algoritmo de forma más eficiente posible.
El ingreso de los valores de la matriz debe ser pedido por teclado. Ten en cuenta casos para que sea
mutante y casos en los que no lo sea.
Una vez cargada correctamente la misma (esto debe verificarse), aplique la función que verifica si hay
presencia de genes mutantes o no y mostrar el resultado por pantalla al usuario.
Subir a Github el proyecto con los casos de prueba."""


# Casos de prueba (deben ingresarse por teclado)):
# Los que salen en el pdf de la consigna:
# dna = ['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG'] = Es Mutante.
# dna = ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG' ] = No es Mutante.
# Casos de prueba que hice:
# dna = ['CTAGTA','GAGCGC','TTCTGT','AGAAAG','CCCACT','TCACGT'] = No es Mutante.
# dna = ['ATCGTC','CAGTGA','TTCTGG','AGAAGG','CCCTTG','TCACTG'] = No es Mutante.
# dna = ['ATGCGA','CTGAGC','TTATGT','AGTAAG','CTCTTA','TCAAAA'] = Es Mutante.


# Importamos todas las funciones desde el archivo funcionesParcial2.
from funcionesParcial2 import * 

# Crear una matriz 6x6 de ADN.
dna = []
for i in range(6):
    sequence = enter_sequence()
    dna.append(list(sequence))  # Convierte la cadena en una lista de caracteres.

# Imprimir la matriz en formato 6x6.
print_matrix(dna)

# Llamar a la función is_mutant con la matriz ingresada.
if is_mutant(dna):
    print("Es un mutante.")
else:
    print("No es un mutante.")
