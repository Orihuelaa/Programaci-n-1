import random #se importa un módulo llamado "random", que proporciona funciones relacionadas con la generación de números aleatorios y selección aleatoria de elementos de secuencias.

# Lista de palabras predefinidas.
words = ["python", "programacion", "tecnologia", "desarrollo", "inteligencia", "computadora"]

# Función para seleccionar una palabra al azar.
def select_word():
    return random.choice(words) #choice() es parte del módulo random en Python y se utiliza para seleccionar aleatoriamente un elemento de una secuencia (como una lista, tupla o cadena).

# Función para inicializar el tablero.
def initialise_board(word):
    return ["_" for _ in word] #itera a través de cada letra de la palabra que se pasa como argumento, creando un número igual de guiones bajos como letras en la palabra.

# Función para mostrar el tablero actual.
def show_board(board):
    return " ".join(board) #join() se utiliza para combinar los elementos de una secuencia (como una lista, tupla o conjunto) en una sola cadena de texto. 
#Estamos uniendo los elementos del tablero con un espacio en blanco " ", para que el contenido del tablero sea mas facil de leer.

# Función principal del juego.
def hanged():
    secret_word = select_word()
    attempts_remaining = 6
    guessed_letters = []
    board = initialise_board(secret_word)
    
    print("¡Bienvenido al Juego del Ahorcado!")
    print("Tienes que adivinar una palabra relacionada con la tecnología.")
    
    while True:
        # Muestra el estado actual del tablero del juego.
        print("\n" + show_board(board))
        # Solicita al jugador ingresar una letra y la convierte a minúsculas.
        letter = input("\nIngresa una letra: ").lower()
        
        # Verifica que la entrada sea una letra y que la longitud de la cadena letra sea exactamente 1.
        if not letter.isalpha() or len(letter) != 1:
            print("¡Caracter erroneo!, ingrese una sola letra.")
            continue

        # Verifica si la letra ya ha sido adivinada previamente.
        if letter in guessed_letters:
            print("Ya adivinaste esa letra.")
            continue
        
        # Verifica si la letra ingresada está en la palabra secreta.
        if letter in secret_word:

            guessed_letters.append(letter) # Agrega la letra a la lista de letras adivinadas.

            # Actualiza el tablero con la letra adivinada en las posiciones correctas.
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    board[i] = letter
            print("Adivinaste una letra correctamente.")

        else:
            attempts_remaining -= 1 #Reduce el número de intentos restantes en caso de una adivinanza incorrecta.
            print(f"Letra incorrecta, te quedan {attempts_remaining} intentos.")
        
        # Verifica si ya se adivinaron todas las letras en el tablero.
        if "_" not in board:
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            print(f"La palabra era: {secret_word}")
            break

        # Verifica si se han agotado los intentos restantes.
        if attempts_remaining == 0:
            print("\n¡Has agotado tus intentos! Perdiste.")
            print(f"La palabra era: {secret_word}")
            break

# Iniciar el juego.
hanged()