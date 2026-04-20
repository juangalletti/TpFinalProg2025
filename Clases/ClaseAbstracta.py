from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo,patente):
        self.marca = marca
        self.modelo = modelo
        
        self.__patente= None
        self.patente= patente
    
    @property
    def patente(self):
        return self.__patente
    
    @property
    def mostrarPatente(self):
        return f" La patente de el vehículo {self.marca} {self.modelo} es {self.__patente}"
    
    @patente.setter
    def patente(self, nueva_patente):
        while True:
            nueva_patente = nueva_patente.strip().upper()
            if len(nueva_patente) == 6 and nueva_patente.isalnum():
                self.__patente = nueva_patente
                break
            else:
                print("La patente debe tener exactamente 6 caracteres alfanuméricos (letras y números).")
                nueva_patente = input("Ingrese nuevamente la patente: ")
                
    @abstractmethod
    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} ha arrancado.")

    @abstractmethod
    def tipo(self):
        pass
