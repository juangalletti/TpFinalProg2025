from Clases.Auto import *
from Clases.Moto import *
from Clases.Colectivo import *
from Clases.AutoHibrido import *
from Clases.AutoElectrico import *
from Clases.Furgon import *
from Clases.ClaseAbstracta import *
from Utils.utils import *

cargar_vehiculos()

tipo_actual = None


def seleccionar_tipo():

    global tipo_actual
    while True:
        print("\nSELECCIONAR TIPO DE VEHÍCULO")
        print("a. Auto")
        print("b. Moto")
        print("c. Colectivo")
        print("d. Auto híbrido")
        print("e. Auto Electrico 100%")
        print("f. Furgon")
        print("g. Mostrar todos")        
        opcion = input("Elegí una opción: ").lower()

        if opcion == "a":
            tipo_actual = "auto"
        elif opcion == "b":
            tipo_actual = "moto"
        elif opcion == "c":
            tipo_actual = "colectivo"
        elif opcion == "d":
            tipo_actual = "autohibrido"
        elif opcion == "e":
            tipo_actual = "autoelectrico"
        elif opcion == "f":
            tipo_actual = "furgon"
        elif opcion== "g":
            tipo_actual ="todos"
        else:
            print("Opción inválida. Intentá nuevamente.")
            continue

        print(f"\n Tipo seleccionado: {tipo_actual.upper()}")
        break


def menu():
    while True:

        if tipo_actual == "todos":
            VehiculosArrancarTodos()
            seleccionar_tipo()   
            continue

        print(f"\nMENÚ PRINCIPAL ({tipo_actual.upper()}) ")
        print(f"1. Crear {tipo_actual.upper()}")
        print(f"2. Mostrar {tipo_actual.upper()}")
        print(f"3. Mostrar Patentes")
        print(f"4. Modificar {tipo_actual.upper()}")
        print(f"5. Eliminar {tipo_actual.upper()}")
        print(f"6. Cambiar tipo de vehiculo")
        print(f"7. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            crear_vehiculo(tipo_actual)
        elif opcion == "2":
            mostrar_vehiculo(tipo_actual)
        elif opcion == "3":
            Patente_mostrar(tipo_actual)
        elif opcion == "4":
            modificar_vehiculo(tipo_actual)
        elif opcion == "5":
            eliminar_vehiculo(tipo_actual)
        elif opcion == "6":
            seleccionar_tipo()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


seleccionar_tipo()
menu()