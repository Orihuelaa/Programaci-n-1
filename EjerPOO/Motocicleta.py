class Motorcycle:
    # Atributo de clase para especificar que todas las motocicletas son nuevas
    new = True
    
    # Atributo de clase para especificar si el motor está en marcha o detenido
    engine = False

    def __init__(self, colour, tuition, fuel_litres, number_wheels, brand, model, date_manufacture, top_speed, weight):
        self.colour = colour
        self.tuition = tuition
        self.fuel_litres = fuel_litres
        self.number_wheels = number_wheels
        self.brand = brand
        self.model = model
        self.date_manufacture = date_manufacture
        self.top_speed = top_speed
        self.weight = weight

    def start(self):
        if self.engine:
            print("El motor ya estaba en marcha.")
        else:
            self.engine = True
            print("El motor ha arrancado.")

    def stop(self):
        if self.engine:
            self.engine = False
            print("El motor se ha detenido.")
        else:
            print("El motor ya estaba detenido.")

    def consult_price(self):
        return self.price

