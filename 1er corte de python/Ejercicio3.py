
""""" Este es el archivo principal donde solo llamamos a la funcion del modulo
El programa permite al usuario ingresar un numero y ver su conversion a binario,
ademas de visualizar si la pila esta vacia y mostrar su contenido. """""

from ModuloEjercicio3 import Pila, Convbinario  # Importamos las clases desde el módulo

def menu():
    pila = Pila()  # Creamos una instancia de la pila

    while True:
        print("\nMENÚ:")
        print("1. Agregar número a la pila")
        print("2. Ver pila")
        print("3. Eliminar el último número de la pila")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                numero = int(input("Ingrese un número entero: "))
                binario = Convbinario.convertir(numero)  # Usamos la clase Convbinario
                pila.apilar(numero, binario)
                print(f"Se agregó: {numero} → {binario}")
            except ValueError:
                print("⚠️ Error: ingrese un número entero válido.")
        elif opcion == '2':
            pila.mostrar()
        elif opcion == '3':
            if pila.es_vacia():
                print("La pila está vacía. No hay elementos para eliminar.")
            else:
                eliminado = pila.cima
                pila.cima = pila.cima.siguiente
                print(f"Elemento eliminado: Decimal {eliminado.dato} → Binario {eliminado.binario}")
        elif opcion == '4':
            print("Gracias por usar el programa. Hasta luego.")
            break
        else:
            print("Opcion no válida. Intente de nuevo.")

# Esto permite que el programa corra solo el archivo principal 
if __name__ == "__main__":
    menu()
