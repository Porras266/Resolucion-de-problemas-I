"""Buenos dias profe somos Nicole Ramos , Allysson Palma y Andres Porras
4/30/2025
Este es el ejercicio #2 de la presentacion de power point
EJERCICIO: Implementa un método llamado “ordena” que reciba una pila de enteros como parámetro 
y devuelva la pila ordenada de mayor (fondo de la pila) a menor (top de la pila).
"""

from ejer2pilas import Pila

# Crear una nueva pila vacía
mi_pila = Pila()

# Pedir al usuario que ingrese los números separados por comitas
entrada = input("Ingrese los números separados por comas (ej: 5,2,8,1): ")

# Separar los números y los convierte en enteros
numeros = entrada.split(",")
for n in numeros:
    n = n.strip()              # este cosito Quita espacios en blanco
    if n.isdigit():            # Verificamos si el número es válido
        mi_pila.push(int(n))   # Agrega el número a la pilita

# muestra la pila original
print("Pila original (de tope a fondo):")
print(mi_pila.mostrar())

# Ordena la pila usando el método 'ordena'
pila_ordenada = Pila.ordena(mi_pila)

# Mostrar la pila ordenada por decirlo asi 
print("Pila ordenada (de tope a fondo):")
print(pila_ordenada.mostrar())
