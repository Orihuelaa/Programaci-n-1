def main():  #Es el punto de entrada principal, donde se inicia la ejecución del programa y coordina las diferentes partes del código. No es necesario usarlo pero es una practica común en Python.

    try: #Se utiliza para definir un bloque de código en el cual se pueden producir excepciones (errores) durante su ejecución, y te permite manejar estas excepciones de manera controlada.

        # Pedir al usuario que ingrese la fecha en el formato indicado
        fecha_actual = input("Ingrese la fecha en formato día, y luego DD/MM: ")
        dia_semana, fecha = map(str.strip, fecha_actual.split(','))#.split(',') sirve para dividir la entrada de fecha_actual en dos partes distintas
        #(dia_semana por un lado y fecha por el otro), utilizando la coma como delimitador.
        #map()aplica una función específica a todos los elementos en un iterable de entrada (como una lista, tupla, etc.) y devuelve un iterador que produce los resultados. Es una función incorporada que se utiliza a menudo para transformar o modificar datos de forma concisa.
        #map()función se usa para aplicar str.strip a cada elemento producido por fecha_actual.split(','). El str.strip() elimina los espacios en blanco iniciales y finales (como espacios y caracteres de nueva línea) de una cadena.
        dia, mes = fecha.split('/')#.split('/') sirve para dividir la entrada de fecha en dos partes distintas (dia por un lado y mes por el otro), utilizando / como delimitador.

        # Convertir a minúsculas para que no genere errores si se utilizan mayusculas.
        dia_semana = dia_semana.lower()

        # Validar el día de la semana y la fecha
        """dia_semana not in dias_semana_validos: Verifica si el día de la semana ingresado no está en la lista de días válidos.
            int(dia) > 31: Verifica si el número de día es mayor que 31, lo que sería un día inválido.
            int(mes) > 12: Verifica si el número de mes es mayor que 12, lo que sería un mes inválido."""
        
        dias_semana_validos = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
        if dia_semana not in dias_semana_validos or int(dia) > 31 or int(mes) > 12:
            print("Error: Fecha o día de la semana inválidos.")
            return   # Finalizar el programa si hay un error
        
        # Procesar según el día de la semana
        if dia_semana in ['lunes', 'martes', 'miércoles']:
                tomar_examenes = input(f"¿Se tomaron exámenes el {dia_semana.title()}? (si/no): ")  #Pregunta si se tomaron exámenes en caso de que sea lunes, martes o miércoles
                if tomar_examenes.lower() == 'si':   # lower() Convertir a minúsculas para que no genere errores si se utilizan mayusculas
                    procesar_examenes()        #Lo que hace este if es que si la respuesta es es igual a si, de que si se tomo examen o no ese dia se ejecute la función procesar_examenes().     
        elif dia_semana == 'jueves':
            procesar_practica_hablada()  # Llamar a la función para procesar práctica hablada
        elif dia_semana == 'viernes':
            procesar_ingles_viajeros(dia,mes)   # Llamar a la función para procesar inglés para viajeros

    except ValueError:
        print("Error: Formato de fecha incorrecto.")  # Capturar el error si ocurre una excepción de tipo ValueError

def procesar_examenes():  #Procesa los resultados de los exámenes.
    aprobaron = int(input("Ingrese la cantidad de alumnos que aprobaron: ")) #Solicita al usuario la cantidad de alumnos que aprobaron.
    total_alumnos = int(input("Ingrese el total de alumnos: "))  #Solicita al usuario la cantidad de alumnos.
    porcentaje_aprobados = (aprobaron / total_alumnos) * 100  #Calcula el porcentaje de aprobados.
    print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")  #Muestra el porcentaje de aprobados.

def procesar_practica_hablada():  # Procesa la asistencia de práctica hablada.
    asistencia = float(input("Ingrese el porcentaje de asistencia: "))  # Solicita al usuario el porcentaje de asistencia.
    if asistencia > 50:  
        print("Asistió la mayoría.")   
    else:
        print("No asistió la mayoría.")

"""El if evalúa la expresión y verifica si el porcentaje de asistencia es mayor que 50. Si esta expresión es verdadera,
el código dentro del bloque if se ejecuta. Imprimiendo el mensaje "Asistió la mayoría.".
El else es opcional y se ejecuta si la expresión en el if es falsa,
si esto ocurre, el código dentro del bloque else se ejecuta. Imprimiendo el mensaje "No asistió la mayoría."."""

def procesar_ingles_viajeros(dia, mes):  #Procesa el ingles para viajeros

    if (dia == '01' and mes == '01') or (dia == '01' and mes == '07'):
        print("Comienzo de nuevo ciclo")
        alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: ")) #Solicita al usuario la cantidad de alumnos que ingresaron al nuevo ciclo.
        arancel_por_alumno = float(input("Ingrese el arancel por alumno en $: "))   #Solicita al usuario el arancel por alumno.
        ingreso_total = alumnos_nuevo_ciclo * arancel_por_alumno  #Calcula el ingreso total por todos los alumnos del nuevo ciclo.
        print(f"Ingreso total en $: {ingreso_total:.2f}")  #Muestra el ingreso total

"""El if evalúa si la fecha ingresada es el 1 de enero o el 1 de julio, 
y si se cumple esa condición, ejecuta el bloque de código dentro del if."""


if __name__ == "__main__":  #Es una convención (regla o práctica) en Python que permite determinar si el archivo actual se está ejecutando como el programa principal o si está siendo importado como un módulo en otro archivo.
    main()   # Llamar a la función principal para iniciar el programa.
