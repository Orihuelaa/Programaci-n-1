from Motocicleta import Motorcycle

motorbike1=Motorcycle('Blanco','A123BCD', 10, 2, "Honda", "CBR600", "2022", 200, 150)

# Prueba de arrancar el motor
print("Prueba de arrancar el motor:")
motorbike1.start()  # Debería mostrar "El motor ha arrancado."
motorbike1.start()  # Debería mostrar "El motor ya estaba en marcha."

# Prueba de detener el motor
print("\nPrueba de detener el motor:")
motorbike1.stop()  # Debería mostrar "El motor se ha detenido."
motorbike1.stop()  # Debería mostrar "El motor ya estaba detenido."

# Agregar el precio a la motocicleta
motorbike1.price = 5000  # Aquí asignamos un precio de $5000 a moto1

# Imprimir el valor del precio
#print(f"El precio de la motocicleta {motorbike1.brand} {motorbike1.model} es de ${motorbike1.price}.") otra forma.

print(f"El precio de la motocicleta {motorbike1.brand} {motorbike1.model} es de ${motorbike1.consult_price()}.")

motorbike2 = Motorcycle('Rojo', 'B456EFG', 8, 2, "Suzuki", "GSX-R750", "2021", 220, 160)

# Consultar el precio de la segunda motocicleta
print(f"El precio de la motocicleta {motorbike2.brand} {motorbike2.model} es de $ {motorbike2.consult_price()}.")
