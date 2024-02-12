import Datas.modulos.Funciones_campers as FCRUD
from os import system

def mostrar_menu():
    print("\nBienvenido usuario, ¿que deseas Hacer el día de hoy?")
    print("1. Acceder al menú de campers ")
    print("2. Acceder al menú de trainers ")
    print("3. Salir")

def menu_campers():
    print("\nMenú de Campers:")
    print("1. Agregar nuevo camper")
    print("2. Mostrar información de campers")
    print("3. Actualizar información de campers ya registrados")  
    print("4. Atrás")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        system("clear")
        if opcion == '1':
            while True:
                menu_campers()
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    FCRUD.agregar_camper()
                elif opcion == '2':
                    FCRUD.mostrar_info_campers()
                elif opcion == '3':
                    FCRUD.actualizar_campers()
                elif opcion == '4':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        elif opcion == '2':
            print("en mantenimiento")
        elif opcion == '3':
            print("¡Hasta luego usuario! ")
            break    
        else:
            print("la opcion ingresada no es válida, por favor ingresa una de las opciones disponibles. ")     

if __name__ == "__main__":
    main()
 