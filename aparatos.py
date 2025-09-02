# Clase que guarda los datos de un aparato eléctrico
class Aparato:
    def __init__(self, nombre, potencia, horas, costo_kwh):
        self.nombre = nombre
        self.potencia = potencia      # en watts
        self.horas = horas            # horas al mes
        self.costo_kwh = costo_kwh    # costo por kWh

    # Método para calcular consumo en kWh
    def consumo(self):
        return (self.potencia * self.horas) / 1000
    
    # Método para calcular el costo en $
    def costo(self):
        return self.consumo() * self.costo_kwh
    
    # Mostrar datos en texto
    def info(self):
        return (f"Aparato: {self.nombre} | Potencia: {self.potencia}W | "
                f"Horas: {self.horas} | Consumo: {self.consumo():.2f} kWh | "
                f"Costo: ${self.costo():.2f}")
