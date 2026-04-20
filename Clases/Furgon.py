from Clases.Colectivo import Colectivo
from Clases.Auto import Auto


#Aplico Herencia Hibrida
class Furgon(Colectivo, Auto):
    def __init__(self, marca, modelo, patente, capacidad, puertas):
        Colectivo.__init__(self, marca, modelo, patente, capacidad)
        Auto.__init__(self, marca, modelo, patente, puertas)

    def tipo(self):
        print(f"Soy un FURGÓN -> {self.marca} {self.modelo} | {self.capacidad} capacidad | {self.puertas} puertas")
