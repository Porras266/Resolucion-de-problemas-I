# estructura_pila.py

def separarParImpar(pila):
    """Separa los números pares e impares en una pila.
    Los pares quedan abajo y los impares arriba."""
    
    pila_pares = []
    pila_impares = []

    # Separar en dos pilas auxiliares
    while pila:
        numero = pila.pop()
        if numero % 2 == 0:
            pila_pares.append(numero)
        else:
            pila_impares.append(numero)

    # Reconstruir pila: primero pares, luego impares
    for numero in reversed(pila_pares):
        pila.append(numero)
    for numero in reversed(pila_impares):
        pila.append(numero)

    return pila
