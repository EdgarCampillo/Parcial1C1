# Importamos las clases desde los otros archivos
from aparatos import Aparato
from consumo import Consumo

# Lista para guardar los aparatos
aparatos = []

# Pedimos al usuario cuántos aparatos quiere registrar
cantidad = int(input("¿Cuántos aparatos desea registrar?: "))

# Ciclo para pedir datos de cada aparato
for i in range(cantidad):
    print(f"\nAparato {i+1}")
    nombre = input("Nombre del aparato: ")
    potencia = float(input("Potencia en watts: "))   # ejemplo: 100, 200, etc.
    horas = float(input("Horas de uso al mes: "))   # ejemplo: 50, 100
    costo_kwh = float(input("Costo por kWh en $: ")) # ejemplo: 0.20
    
    # Creamos un aparato y lo guardamos en la lista
    aparato = Aparato(nombre, potencia, horas, costo_kwh)
    aparatos.append(aparato)

# Creamos un resumen con todos los aparatos
consumo = Consumo(aparatos)

# Mostramos el detalle de cada aparato
print("\n--- Detalle de consumo ---")
for a in aparatos:
    print(a.info())

# Mostramos el resumen total
print("\n--- Resumen total ---")
print(f"Consumo total (kWh): {consumo.consumo_total():.2f}")
print(f"Gasto total ($): {consumo.costo_total():.2f}")
