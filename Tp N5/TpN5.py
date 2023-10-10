import funciones

"""1. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos."""

dni = input("Ingrese su número de DNI: ")

#Verificar si el número de DNI es válido
print(funciones.validate_dni(dni))

"""2. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. 
También podría haber espacios al principio o al final del string pasado por parámetro."""

chain = input("Ingresa una cadena de texto: ")

# Llama a la función para obtener la longitud de la última palabra
length = funciones.last_word_length(chain)

print(f"Longitud de la última palabra: {length}")


"""3. Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y 
número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, 
apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y 
los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254"""

while True:
    full_name = input("Ingrese el nombre completo del socio (o nombre vacío para finalizar): ").title()
    #Verificar si el nombre está vacío para finalizar el programa
    if not full_name:
        break
    #Validar DNI
    dni = funciones.get_valid_dni()
    
    #Generar el identificador único del socio
    identifier= funciones.generate_identifier(full_name, dni)
    print(f"ID -> {identifier}")

"""4. Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""

num1 = funciones.get_valid_integer("Ingrese el primer número entero: ")
num2 = funciones.get_valid_integer("Ingrese el segundo número entero: ")

#Llamar a la función "en_multiplo" para verificar si el primer número es múltiplo del segundo
if funciones.en_multiplo(num1, num2):
    print(f"{num1} es múltiplo de {num2}.")
#Verificar si el segundo número es múltiplo del primero
elif funciones.en_multiplo(num2, num1):
    print(f"{num2} es múltiplo de {num1}.")
else:
    print("Ninguno de los números es múltiplo del otro.")


"""5. Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y 
vaya mostrando la media. El programa pedirá el número de días que se van a introducir."""

number_of_days = funciones.get_valid_integer("Ingrese el número de días: ")

#Iterar a través de los días y calcular la temperatura media para cada uno
for day in range(1, number_of_days + 1):
    temp_max = funciones.get_valid_number(f"Ingrese la temperatura máxima del día {day}: ")
    temp_min = funciones.get_valid_number(f"Ingrese la temperatura mínima del día {day}: ")
    #Llamar a la función "calculate_temp_half" para calcular la temperatura media del día
    temp_half = funciones.calculate_temp_half(temp_max, temp_min)
    print(f"La temperatura media del día {day} es: {temp_half}°C")

"""6. Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""

# Solicitamos al usuario que ingrese un texto
text = input("Ingrese un texto: ")

# Llamamos a la función para agregar espacios entre letras
result = funciones.add_space_between_letters(text)

# Mostramos el resultado en pantalla
print("Texto con espacios adicionales entre letras:")
print(result)

"""7. Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa 
que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""

numbers = []  #Inicializamos una lista vacía para almacenar los números ingresados
    
#Solicitamos al usuario que ingrese números hasta que ingrese un valor no numérico
while True:
    number = funciones.get_valid_number("Ingrese un número (ingrese 0 para salir): ")  # Utilizamos la función para obtener un número válido
    if number == 0:
        break  # Si el usuario ingresa 0, salimos del bucle
    numbers.append(number)  # Agregamos el número a la lista

#Luego de salir del bucle, calculamos el máximo y mínimo
if numbers:
    max, min = funciones.find_max_min(numbers)
    print(f"El número máximo es: {max}")
    print(f"El número mínimo es: {min}")
else:
    print("No se ingresaron números.")

"""8. Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal 
que lea el radio de una circunferencia y muestre su área y perímetro."""

# Solicitamos al usuario que ingrese el radio de la circunferencia
radius = funciones.get_valid_number("Ingrese el radio de la circunferencia: ")
# Validamos que el radio sea positivo
if radius <= 0:
    print("El radio debe ser un número positivo. Intente nuevamente.")
else:
# Llamamos a la función para calcular el área y el perímetro
    area, perimeter = funciones.calculate_area_perimeter(radius)

# Mostramos los resultados
    print(f"Área de la circunferencia: {area:.2f}")
    print(f"Perímetro de la circunferencia: {perimeter:.2f}")

"""9. Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario 
es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer 
login incremente este valor. Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo."""

#Inicializar el contador de intentos de login
attempts = 0

while attempts < 3:  # Permitimos hasta tres intentos
    # Solicitamos al usuario que ingrese el nombre de usuario y la contraseña
    user = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    # Llamamos a la subrutina login para verificar el login
    result, attempts = funciones.login(user, password, attempts)

#Verificar el resultado del intento de login
    if result:
        print("True")
        break
    else:
        print("Login fallido. Intente nuevamente.")
        if attempts < 3:
            print(f"Le quedan {3 - attempts} intentos restantes.")
        else:
            print("Se agotaron los intentos. Acceso bloqueado.")

"""10. Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y 
porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra."""

#Crear un diccionario vacío para representar el carrito de compra
shopping_cart = {}
#Iniciar un bucle para agregar productos al carrito
while True:
    product_name = input("Ingrese el nombre del producto (si el producto tiene descuento colocar al final del nombre del producto '_descuento'y fin para terminar): ")

    if product_name.lower() == 'fin': #Verificar si el usuario desea terminar la entrada de productos
        break

    product_price = funciones.get_valid_number("Ingrese el precio del producto: ")
    discount_percentage = funciones.get_valid_number("Ingrese el porcentaje de descuento (0 si no hay descuento): ")

# Agregar el producto al carrito con su precio y, si hay descuento, incluir el porcentaje de descuento en el nombre
    if discount_percentage > 0:
        shopping_cart[f"{discount_percentage}_descuento_{product_name}"] = product_price
    else:
        shopping_cart[product_name] = product_price

#Llamar a una función "apply_discount" para aplicar los descuentos y calcular el precio final de la compra
final_price = funciones.apply_discount(shopping_cart)
print(f"Precio final de la compra: {final_price:.2f}")

"""11. Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos 
de la lista."""

#Crear una lista vacía para almacenar los números ingresados
numbers = []
while True:
    try:
        numbers_quantity = int(input("Ingrese la cantidad de números que desea procesar: "))
        break
    except ValueError:
        print("Ingrese un número válido para la cantidad.")

#Solicitar al usuario ingresar los números y agregarlos a la lista
for i in range(numbers_quantity):
    while True:
        try:
            number = int(input(f"Ingrese el número {i + 1}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Ingrese un número válido.")

#Llamar a una función "apply_function_to_list" para aplicar la función "square" a cada número en la lista
results = funciones.apply_function_to_list(funciones.square, numbers)
print("Resultados:", results)

"""12. Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""

while True:
    sentence = input("Ingrese una frase (o 'fin' para salir): ")
    if sentence.lower() == 'fin': #Verificar si el usuario desea salir del programa
            break
    #Verificar si la frase está vacía y solicitar al usuario que ingrese una frase válida
    if not sentence:
        print("La frase no puede estar vacía. Intente de nuevo.")
        continue
    #Obtener un diccionario con las palabras y sus longitudes utilizando la función "get_word_length" 
    result = funciones.get_word_length(sentence)
    print("Palabras y sus longitudes:")
    #Iterar a través del diccionario y mostrar cada palabra y su longitud
    for word, length in result.items():
# items() devuelve una vista de los elementos del diccionario como tuplas clave-valor. Esta vista es iterable, lo que significa que puedes recorrerla en un bucle.
        print(f"{word}: {length}")

"""13. Escribir una función que calcule el módulo de un vector."""

while True:
    try:
        x = float(input("Ingrese la componente x del vector: "))
        y = float(input("Ingrese la componente y del vector: "))
        z = float(input("Ingrese la componente z del vector: "))
        #Calcular el módulo del vector utilizando una función "calculate_module_vector"
        module = funciones.calculate_module_vector(x, y, z)
        print(f"El módulo del vector ({x}, {y}, {z}) es: {module:.2f}")
        break
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números válidos para las componentes x, y y z.")

"""14. Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida."""

try:
    number = int(input("Ingrese un número entero: "))
    if funciones.cousin(number): #Verifica si el número ingresado es primo utilizando la función "cousin"
        print(f"{number} es un número primo.")
    else:
        print(f"{number} no es un número primo.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número entero válido.")

"""15. Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. 
Utilizar una o más funciones, según sea necesario."""

read_numbers = 0
    
while True:
    try:
        number = int(input("Ingrese un número entero positivo (o ingrese 0 para terminar): "))
        #Validar que el número ingresado sea positivo
        if number < 0:
            print("El número debe ser positivo.")
            continue
        elif number == 0:
            break
        read_numbers += 1 #Incrementar el contador de números leídos
        result = funciones.factorial(number) #Calcular el factorial del número utilizando una función "factorial"
        print(f"El factorial de {number} es {result}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero positivo o 0 para terminar.")
        
    print(f"Total de números leídos: {read_numbers}")

"""16. Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, 
utilizando para ello una función que calcule la frecuencia."""

try:
    number = int(input("Ingrese un número entero: "))
    digit = int(input("Ingrese un dígito: "))
    
    if digit < 0 or digit > 9: #Validar que el dígito esté en el rango de 0 a 9
        print("El dígito debe estar en el rango de 0 a 9.")
    # Calcular la frecuencia de ocurrencias del dígito en el número utilizando una función "count_occurrences_digits"
    frequency = funciones.count_occurrences_digits(number, digit)
    # Verificar si el dígito aparece o no en el número
    if frequency == 0: 
        print(f"El dígito {digit} no aparece en el número {number}.")
    else:
        print(f"El dígito {digit} aparece {frequency} veces en el número {number}.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número entero y un dígito válido.")

"""17. Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. 
Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de 
veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado."""

#Inicializar variables
cousin_older = 0
largest_factorial = 1
while True:
    try:
        number = int(input("Ingrese un número primo (o un número no primo para finalizar): "))
        
        if number <= 0: #Validar que el número ingresado sea positivo
            print("El número debe ser positivo.")
            continue

        if not funciones.cousin(number): #Comprobar si el número ingresado no es primo (usando la función "cousin")
            break

        digits_sum = funciones.calculate_sum_digits(number) #Calcular la suma de los dígitos del número ingresado
        print(f"La suma de los dígitos de {number} es {digits_sum}")

        digit = int(input("Ingrese un dígito: "))
        # Calcular la cantidad de veces que aparece el dígito en el número ingresado
        frequency = funciones.count_occurrences_digits(number, digit)
        print(f"El dígito {digit} aparece {frequency} veces en {number}")

        if number > cousin_older: #Actualizar el valor de "cousin_older" si el número ingresado es mayor
            cousin_older = number

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número primo válido.")

if cousin_older > 0: #Calcular el factorial del primo mayor ingresado
    largest_factorial = funciones.factorial(cousin_older)

print(f"Factorial del mayor número primo ingresado: {largest_factorial}")