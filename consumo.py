# Clase que calcula totales de todos los aparatos
class Consumo:
    def __init__(self, aparatos):
        self.aparatos = aparatos

    # Suma el consumo de todos
    def consumo_total(self):
        return sum(a.consumo() for a in self.aparatos)

    # Suma el costo de todos
    def costo_total(self):
        return sum(a.costo() for a in self.aparatos)
