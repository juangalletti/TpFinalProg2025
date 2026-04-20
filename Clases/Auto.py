from Clases.ClaseAbstracta import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo,patente, puertas):
        super().__init__(marca, modelo,patente)
        self.puertas = puertas  

    def tipo(self):
        print(f"Soy un auto {self.marca} {self.modelo} con {self.puertas} puertas.")

    def arrancar(self):
        print(f"El Auto {self.marca} {self.modelo} ha arrancado.")

#autos = []
