from Clases.Electrico import *
from Clases.Inteligente import *

#Aplico Herencia Multiple
class AutoElectrico(Electrico, Inteligente):
    def __init__(self, marca, modelo, patente, bateria, sistema_autopilot):
        Electrico.__init__(self, bateria)      
        Inteligente.__init__(self, sistema_autopilot)  
        self.marca = marca
        self.modelo = modelo
        self.patente= patente

    def info(self):
        print(f"{self.marca} {self.modelo} - {self.bateria} kWh - Autopilot: {self.sistema_autopilot}")

    def mospaten(self):
        return f" La patente de el vehículo {self.marca} {self.modelo} es {self.patente}"
    
    def arrancar(self):
        print(f"El Auto {self.marca} {self.modelo} ha arrancado.")