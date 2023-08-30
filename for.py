"""Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje considerando la posición de cada una en el alfabeto una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación."""

def cifra_cesar(mensaje, corrimiento):
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    texto_encriptado = ''

    for letra in mensaje: #Recorre a través de cada letra en el mensaje 
        if letra.isalpha(): # Verifica si es una letra
            indice = (alfabeto.index(letra.upper()) + corrimiento) % 27 #convierte la letra en mayúscula usando letra.upper() para asegurarse de que coincida con las letras en alfabeto. Luego, encuentra la posición de esta letra en el alfabeto utilizando alfabeto.index(). Luego, agrega el valor de corrimiento para obtener la posición después del desplazamiento y finalmente se toma el resultado de la suma y se le aplica el operador %27, esto permite que al superar el límite del alfabeto, el índice debe volver al principio.
            if letra.isupper(): # Si la letra original es mayúscula
                texto_encriptado += alfabeto[indice] #Agrega letra cifrada en mayúscula
            else:
                texto_encriptado += alfabeto[indice].lower() #Agrega la letra cifrada en minúscula
        else:
            texto_encriptado += letra # Mantiene caracteres que no son letras

    return texto_encriptado   # Devuelve el mensaje cifrado

corrimiento = int(input("Ingrese el corrimiento (cantidad de lugares que se correrán las letras): "))
mensajes = []

for i in range(5):
    mensaje = input(f"Ingrese el mensaje {i+1}: ")
    mensajes.append(mensaje) # Agrega el mensaje a la lista 'mensajes'

print("\nMensajes encriptados:")
for mensaje in mensajes:
    mensaje_encriptado = cifra_cesar(mensaje, corrimiento) #Aplica cifrado César al mensaje
    print(mensaje_encriptado)
