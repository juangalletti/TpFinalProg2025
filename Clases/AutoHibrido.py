from Clases.ClaseAbstracta import Vehiculo
from Clases.Auto import *
from Clases.Electrico import *


class AutoHibrido(Auto, Electrico):
    def __init__(self, marca, modelo,patente, puertas, bateria):
        Auto.__init__(self, marca, modelo,patente, puertas)
        Electrico.__init__(self, bateria)
        
    def arrancar(self):
        print(f"El Auto Hibrido {self.marca} {self.modelo} ha arrancado.")
    
    def tipo(self):
        print(f"Soy un auto híbrido {self.marca} {self.modelo} con {self.puertas} puertas y una batería de {self.bateria} kWh.")

AutHibr = []
