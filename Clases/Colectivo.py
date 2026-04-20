from Clases.ClaseAbstracta import Vehiculo

class Colectivo(Vehiculo):
    def __init__(self, marca, modelo, patente, capacidad):
        Vehiculo.__init__(self, marca, modelo, patente)   # <-- usar llamada directa
        self.capacidad = capacidad  
        
    def tipo(self):
        print(f"Soy un colectivo {self.marca} {self.modelo} con capacidad para {self.capacidad} pasajeros.")

    def arrancar(self):
        print(f"El Colectivo {self.marca} {self.modelo} ha arrancado.")

colectivos=[]

