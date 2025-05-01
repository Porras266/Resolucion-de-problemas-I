""""" Buenos diasprofe somos Allysson, Nicole y Andres  
30/04/2025

Este es el ejerccico 3 de la presentacion el caul nos indica:Diseñar un método “Convbinario” que reciba un entero como parámetro
 La función, usando una pila, deberá mostrar el número en código binario.
"""""
# Creacion del clasde nodo para nuestra lista enlazada 
class Nodo:
    def __init__(self, dato, binario):
        self.dato = dato  # El número original
        self.binario = binario  # El número en binario
        self.siguiente = None

#Creacion de la calse pila  
class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, dato, binario):
        nuevo_nodo = Nodo(dato, binario)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def es_vacia(self):
        return self.cima is None

    def mostrar(self):
        if self.es_vacia():
            print("La pila está vacía.")
        else:
            print("Contenido de la pila:")
            actual = self.cima
            while actual:
                print(f"Decimal: {actual.dato} → Binario: {actual.binario}")
                actual = actual.siguiente

# Creacion de la funcion binario que nos ayudara a convertir el numero decimal a binario
class Convbinario:
    def convertir(numero):
        if numero == 0:
            return "0"
        binario = ""
        while numero > 0:
            binario = str(numero % 2) + binario
            numero //= 2
        return binario
