import math
#Ejer 1
def validate_dni(dni):
    # Verifica que el DNI tenga entre 7 y 8 dígitos
    if len(dni) < 7 or len(dni) > 8:
        return False

    # Verifica que todos los caracteres del DNI sean dígitos
    if not dni.isdigit():
        return False

    # Si pasa ambas validaciones, el DNI es válido
    return True

#Ejer 2
def last_word_length(chain):
    # Elimina espacios en blanco al principio y al final de la cadena
    chain = chain.strip()
    
    # Divide la cadena en palabras utilizando espacios como separadores
    words = chain.split()
    
    # Verifica si hay palabras en la cadena
    if len(words) == 0:
        return 0  # No hay palabras en la cadena
    
    # La última palabra estará en el índice -1 de la lista de palabras
    last_word = words[-1]
    
    # Retorna la longitud de la última palabra
    return len(last_word)

#Ejer 3
def generate_identifier(full_name, dni):
    # Dividir el nombre completo en palabras
    words = full_name.split()
    
    # Obtener el primer nombre
    first_name = words[0]
    
    # Obtener el apellido
    surname = words[-1]
    
    # Obtener los 3 primeros dígitos del DNI
    first_three_digits = str(dni)[:3]
    
    # Crear el identificador único
    identifier = f"{first_name}{len(surname)}{first_three_digits}"
    
    return identifier

def get_valid_dni():
    while True:
        dni = input("Ingrese el número de DNI (7 u 8 dígitos): ")
        #Verificar si la longitud del DNI es 7 u 8 dígitos y si todos los caracteres son dígitos
        if len(dni) in (7, 8) and dni.isdigit():
            return int(dni) #Si el DNI cumple con los requisitos, convertirlo a entero y devolverlo
        else:
            print("El DNI ingresado no es válido. Debe tener 7 u 8 dígitos.")

#Ejer 4
def en_multiplo(number1, number2):
    if number2 == 0:
        return False  # Evitar la división por cero
    return number1 % number2 == 0

def get_valid_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

#Ejer 5

def calculate_temp_half(temp_max, temp_min):
    #Calcular la temperatura media como el promedio entre la temperatura máxima y mínima
    temp_half = (temp_max + temp_min) / 2
    return temp_half


#Ejer6
def add_space_between_letters(text):
    # Inicializamos una cadena vacía para almacenar el resultado
    result = ""
    
    # Iteramos a través de cada carácter en el texto
    for character in text:
        # Agregamos el carácter actual y un espacio al resultado
        result += character + " "
    
    # Devolvemos el resultado con espacios adicionales
    return result

#Ejer7
def find_max_min(list):
    if not list:
        # Si la lista está vacía, no hay máximo ni mínimo
        return None, None
    
    max = min = list[0]  # Inicializamos con el primer elemento de la lista
    
    #Iterar a través de los números en la lista
    for number in list:
        #Verificar si el número actual es mayor que el máximo actual
        if number > max:
            max = number
        #Verificar si el número actual es menor que el mínimo actual
        elif number < min:
            min = number
    
    return max, min

def get_valid_number(entry):
    while True:
        try:
            number = float(input(entry))  # Intentamos convertir la entrada a un número flotante
            return number  # Devolvemos el número válido
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

#Ejer8
def calculate_area_perimeter(radius):
    # Fórmula para el área de la circunferencia: A = π * r^2
    area = math.pi * radius**2
    
    #Fórmula para el perímetro de la circunferencia (circunferencia): P = 2 * π * r
    perimeter = 2 * math.pi * radius
    #Redondeamos los valores a dos decimales
    area = round(area, 2)
    perimeter = round(perimeter, 2)
    
    return area, perimeter

#Ejer9
def login(user, password, attempts):
    # Verificamos si el usuario y la contraseña son correctos
    if user == "usuario1" and password == "asdasd":
        return True, attempts  # Login exitoso
    else:
        attempts += 1
        return False, attempts  # Login fallido

#Ejer10
def apply_discount(trolley):
    final_price = 0

    for product, price in trolley.items():
        parts = product.split("_")  # Divide el nombre del producto en partes utilizando el guión bajo como separador
        if len(parts) > 2 and parts[-2].isdigit() and parts[-1] == "descuento":
            # Verifica que haya más de dos partes en el nombre del producto,
            # que la penúltima parte sea un dígito (el porcentaje de descuento)
            # y que la última parte sea "descuento"
            discount_percentage = float(parts[-2])  # Obtiene el porcentaje de descuento como número flotante
            final_price += price * (1 - discount_percentage / 100)  # Aplica el descuento al precio
        else:
            final_price += price  # Si no cumple las condiciones anteriores, suma el precio sin descuento

    return final_price


#Ejer11
def apply_function_to_list(function, list):
    #Inicializar una lista vacía para almacenar los resultados
    result = []
    #Iterar a través de cada elemento en la lista
    for element in list:
        # Aplicar la función proporcionada al elemento actual y agregar el resultado a la lista "result"
        result.append(function(element))
    return result

def square(x):
    return x ** 2 #Retorna el cuadrado de "x"

#Ejer12
def get_word_length(sentence):
    #Dividir la frase en palabras utilizando el espacio en blanco como separador
    words = sentence.split()
    #Crear un diccionario para almacenar las palabras y sus longitudes
    dictionary_lengths = {}

    #Iterar a través de las palabras en la lista "words"
    for word in words:
        #Asignar la longitud de cada palabra como el valor en el diccionario, con la palabra como clave
        dictionary_lengths[word] = len(word)

    return dictionary_lengths

#Ejer13
def calculate_module_vector(x, y, z):
    module = math.sqrt(x**2 + y**2 + z**2) # math.sqrt() se utiliza para calcular la raíz cuadrada.
    return module

#Ejer14
def cousin(number):
    if number <= 1:
        return False  #Los números menores o iguales a 1 no son primos

    #Utilizar un bucle para iterar desde 2 hasta la raíz cuadrada del número más 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  #Si el número es divisible por algún número entre 2 y la raíz cuadrada, no es primo

    return True  #Si no se encontraron divisores, es primo

#Ejer15
def factorial(n):
    #Verificar si n es igual a 0, en cuyo caso se devuelve 1
    if n == 0:
        return 1
    else: #Si n no es igual a 0, calcular el factorial recursivamente multiplicando n por el factorial de (n - 1)
        return n * factorial(n - 1)

#Ejer16
def count_occurrences_digits(number, digit):
    #Inicializar una variable "frequency" para contar la frecuencia de aparición del dígito
    frequency = 0
    #Iniciar un bucle mientras el número sea mayor que 0
    while number > 0:
        #Obtener el último dígito del número
        current_digit = number % 10
        #Verificar si el dígito actual es igual al dígito deseado
        if current_digit == digit:
            #Si son iguales, incrementar la frecuencia en 1
            frequency += 1
        # Eliminar el último dígito del número dividiendo entre 10 
        number //= 10
    return frequency

#Ejer17
def calculate_sum_digits(number):
    #Inicializar la variable "sum" para almacenar la suma de los dígitos
    sum = 0
    #Iniciar un bucle mientras el número sea mayor que 0
    while number > 0:
        #Obtener el último dígito del número y sumarlo al total
        sum += number % 10
        #Eliminar el último dígito del número dividiendo entre 10 
        number //= 10
    return sum