"""1. El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, 
y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?:

#DEFINICIÓN DE FUNCIONES

def most(a,b):
if(x>y):
return x
else:
return y

def least(a,b):
if(x<y):
return x
else:
return y

#PROGRAMA PRINCIPAL

x = int(input('Un número:  '))
y = int(input('Otro número:  '))

print(most(x-3, least(x+2, y-5)))"""


# RESPUESTA

"""El problema en el programa es en cómo se definen y utilizan las funciones most y least. 
Las funciones most y least reciben los parámetros a y b, pero dentro de las funciones, estás comparando x e y, 
que son variables globales, en lugar de a y b."""

#DEFINICIÓN DE FUNCIONES

def most(a, b):
    if a > b:
        return a
    else:
        return b

def least(a, b):
    if a < b:
        return a
    else:
        return b

#PROGRAMA PRINCIPAL

x = int(input('Un número:  '))
y = int(input('Otro número:  '))

print(most(x-3, least(x+2, y-5)))
