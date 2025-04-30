"""Ejercicio 3
Clinica que ingresa al sistema nuevos pacientes recorre la lista enlazada 
para mostrarlos, eliminarlos y ordenarlos mediante prioridad del 1 a 5 
"""
#28/04/2025
"""
Andres Porras
Nicolle Ramos
Allyson Palma
"""

#Archivo a importar en el archivo principal
class Nodo:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None

class ListaPacientes:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def insertar_paciente(self, nombre, edad, sintoma, prioridad):
        """Inserta un paciente ordenado por prioridad (1 es más alta)."""
        nuevo = Nodo(nombre, edad, sintoma, prioridad)
    #Caso Si la lista está vacía o si la prioridad del nuevo es más alta que el primero de la lista:
        if self.esta_vacia() or prioridad < self.cabeza.prioridad:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
    #Caso 2: Si hay pacientes y la prioridad es menor (menos urgente) que la del primero:
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
    #Actualiza el tamaño de la lista
        self.tamaño += 1

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
        return self.cabeza is None

    def eliminar_por_nombre(self, nombre):
        """Si la lista está vacía, devuelve False.
        Si el paciente está en la cabeza (primer nodo)
        , lo elimina actualizando la cabeza.
        Si no, recorre la lista con dos punteros: 
        anterior y actual hasta encontrar el nombre y lo saca de la lista. """
        """Elimina un paciente por su nombre (búsqueda exacta)."""
        if self.esta_vacia():
            return False

        if self.cabeza.nombre == nombre:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual is not None:
            if actual.nombre == nombre:
                anterior.siguiente = actual.siguiente
                self.tamaño -= 1
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    def mostrar_pacientes(self):
        """Devuelve una lista de diccionarios con los datos de los pacientes."""
        pacientes = []
        actual = self.cabeza
        while actual is not None:
            pacientes.append({
                'nombre': actual.nombre,
                'edad': actual.edad,
                'sintoma': actual.sintoma,
                'prioridad': actual.prioridad
            })
            actual = actual.siguiente
        return pacientes
