"""
Implementa un método que reciba una pila de enteros como único parámetro. 
Este método llamado “separarParImpar” deberá retornar la pila con los números 
pares en la parte inferior y los impares en la superior.
Ejemplo:
Entrada -> [ 2, 3, 6, 8, 11, 13, 18, 21]
Salida -> [ 2, 6, 8, 18, 3, 11, 13, 21] PARES / IMPARES
"""
"""
Fecha: 30/04/2025
-----------------
Integrantes:
1.Andres Porras 
2.Nicole Ramos 
3.Allyson palma
"""

# programa_principal.py

from Eje1ModuloPilas import separarParImpar

def main():
    # Definir la pila original
    pila_original = [4, 3, 7, 9, 11, 15, 18, 21, 42]
    print(f"Pila original: {pila_original}")

    # Separar pares e impares
    pila_modificada = separarParImpar(pila_original.copy())  # .copy() para no alterar la original
    print(f"Pila después de separar pares e impares: {pila_modificada}")

if __name__ == "__main__":
    main()
