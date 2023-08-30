"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""

def pares_impares(numero):
    pares = 0
    impares = 0
    while numero > 0:
        digito = numero % 10
        if digito == 0:  # condición para excluir el 0 
            impares += 1
        elif digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    return pares, impares

total_pares = 0
total_impares = 0

while True:
    try:
        numero = int(input("Ingrese un número entero positivo (ingrese 0 para finalizar): "))
        if numero < 0:
            print("Por favor, ingrese un número entero positivo.")
            continue
        elif numero == 0:
            break
        pares, impares = pares_impares(numero)
        total_pares += pares
        total_impares += impares
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

print(f"En total, se leyeron {total_pares} dígitos pares y {total_impares} dígitos impares.")