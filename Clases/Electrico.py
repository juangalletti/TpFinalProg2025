

# Clase adicional que representa características eléctricas
class Electrico:
    def __init__(self, bateria):
        self.bateria = bateria  # en kWh

    def cargar_bateria(self):
        print(f"La batería está cargada al {self.bateria} kWh.")
