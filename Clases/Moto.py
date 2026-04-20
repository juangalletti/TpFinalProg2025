from Clases.ClaseAbstracta import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca, modelo, patente, cilindrada):
        super().__init__(marca, modelo,patente)
        self.cilindrada = cilindrada  

    def tipo(self):
        print(f"Soy una moto {self.marca} {self.modelo} de {self.cilindrada} cc.")

    def arrancar(self):
        print(f"La moto {self.marca} {self.modelo} ha arrancado.")  


motos = []
