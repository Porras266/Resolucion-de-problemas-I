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
#Importamos la biblioteca Os 
import os
#Importamos los modulos 
from ModulosEjercicioSemana5 import ListaPacientes

lista_pacientes = ListaPacientes()

def mostrar_menu():
    print("\n=== Sistema de Gestión de Pacientes ===")
    print("1. Registrar nuevo paciente")
    print("2. Eliminar paciente por nombre")
    print("3. Mostrar lista de espera")
    print("4. Salir")

def registrar_paciente():
    print("\n** Registrar Nuevo Paciente **")
    nombre = input("Nombre completo: ")

    while True:
        try:
            edad = int(input("Edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido para la edad.")

    sintoma = input("Síntoma principal: ")

    while True:
        try:
            prioridad = int(input(f"Prioridad (\033[91m1-5, donde 1 es máxima prioridad\033[0m): "))
            if prioridad < 1 or prioridad > 5:
                print("La prioridad debe estar entre 1 y 5.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido para la prioridad.")

    lista_pacientes.insertar_paciente(nombre, edad, sintoma, prioridad)
    print(f"\nPaciente '{nombre}' registrado exitosamente.")
    input("Presione una tecla para continuar")
    os.system('cls')

def eliminar_paciente():
    print("\n** Eliminar Paciente **")
    if lista_pacientes.esta_vacia():
        print("No hay pacientes registrados para eliminar.")
        return

    nombre = input("Ingrese el nombre completo del paciente a eliminar: \n")

    if lista_pacientes.eliminar_por_nombre(nombre):
        print(f"\nPaciente '{nombre}' eliminado exitosamente.")
        input("presione una tecla para continuar")
        os.system('cls')
    else:
        print(f"\nNo se encontró ningún paciente con el nombre '{nombre}'.")
        input("presione una tecla para continuar")
        os.system('cls')

def mostrar_lista():
    print("\n** Lista de Espera **\n")
    pacientes = lista_pacientes.mostrar_pacientes()

    if not pacientes:
        print("No hay pacientes en espera.")
    else:
        print(f"Total de pacientes en espera: {len(pacientes)}")
        for i, paciente in enumerate(pacientes, 1):
            print(f"\nPaciente #{i}:")
            print(f"  Nombre: {paciente['nombre']}")
            print(f"  Edad: {paciente['edad']}")
            print(f"  Síntoma: {paciente['sintoma']}")
                             #Con \003 iniciamos el color 
                             #Con [91m es el color en esquema ansi
                             #al final con \003[0m restablece el color cuando termina en blanco
            print(f"  Prioridad: \033[91m{paciente['prioridad']}\033[0m")
            input("presione una tecla para continuar")

while True:
    mostrar_menu()                            #Elimina Espacios en blanco
    opcion = input("\nSeleccione una opción (1-4): ").strip()

    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        eliminar_paciente()
    elif opcion == "3":
        mostrar_lista()
    elif opcion == "4":
        print("\n¡Gracias por usar el sistema! Hasta pronto.")
        break
    else:
        print("Opción no válida. Por favor ingrese un número del 1 al 4.")

