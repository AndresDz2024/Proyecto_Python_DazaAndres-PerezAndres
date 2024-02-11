import modulos.FuncionesCRUD as funciones

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar nuevo camper")
    print("2. Mostrar información de campers")
    print("3. Agregar nuevo trainer")
    print("4. Mostrar información de trainers")
    print("5. Agregar nuevo coordinador")
    print("6. Mostrar información de coordinadores")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            funciones.agregar_camper()
        elif opcion == '2':
            funciones.mostrar_info_campers()
        #elif opcion == '3':
        #    funciones.agregar_trainer()
       # elif opcion == '4':
      #      funciones.mostrar_info_trainers()
     #   elif opcion == '5':
    #        funciones.agregar_coordinador()
   #     elif opcion == '6':
  #          funciones.mostrar_info_coordinadores()
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
