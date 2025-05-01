"""Buenos dias profe somos Nicole Ramos , Allysson Palma y Andres Porras
4/30/2025
Este es el ejercicio #2 de la presentacion de power point
EJERCICIO: Implementa un método llamado “ordena” que reciba una pila de enteros como parámetro 
y devuelva la pila ordenada de mayor (fondo de la pila) a menor (top de la pila).
"""

# pila.py

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None# varible que apunta al ultimo tope de la pila

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo #actualiza la pilita


      # Devuelve los elementos de la pila como una lista (de arriba hacia abajo)
    def mostrar(self):
        actual = self.cima
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos   # Retorna la lista con los valores

  # Método que ordena una pila de mayor (fondo) a menor (tope)
    def ordena(pila_original):
        # Guardar todos los datos en una lista
        datos = []

         # Recorrer la pilita y guarda los datos  
        actual = pila_original.cima
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente

        # Ordenar de mayor a menor
        datos.sort(reverse=True)

        # Crear nueva pila ordenada
        nueva = Pila()
        for valor in datos:
            nueva.push(valor)

        return nueva  # Retornar la nueva pila ya ordenada
   
    
     



