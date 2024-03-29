import Datas.modulos.Funciones_campers as FCRUD
import Datas.modulos.Funciones_trainers as FCRUD2
import Datas.modulos.Funciones_salones as FCRUD3
import Datas.modulos.Funciones_notas as FCRUD4
import Datas.modulos.Modulo_reportes as RPT
from os import system

def mostrar_menu():
    print("\nBienvenido usuario, ¿que deseas Hacer el día de hoy?")
    print("1. Acceder al menú de coordinadores ")
    print("2. Acceder al menú de trainers ")
    print("3. Acceder al menú de reportes ")
    print("4. Salir")
    
def menu_reportes():
    print("\nMenú de reportes:")
    print("1. Listar los campers que se encuentran en estado inscrito")
    print("2. Listar los campers que pasaron el examen inicial")
    print("3. Listar trainers que se encuentran trabajando en campuslands")
    print("4. Listar los campers que cuentan con bajo rendimiento")
    print("5. Listar los trainers y los campers que se encuentran asociados a una ruta de entrenamiento")
    print("6. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el trainer encargado")
    print("7. volver")    

def menu_trainers():
    print("\nMenú de trainers:")
    print("1. Agregar nuevo trainer")
    print("2. Mostrar información de trainers")
    print("3. asignar la jornada del trainer")
    print("4. Actualizar informaciòn del trainer")
    print("5. volver")    

def menu_coordinadores():
    print("\nMenú de coordinadores:")
    print("1. Agregar nuevo camper")
    print("2. Mostrar información de campers")
    print("3. Actualizar información de campers ya registrados") 
    print("4. Registrar notas prueba de admisión") 
    print("5. Crear nuevo salon")
    print("6. Ingresar camper a un salon")
    print("7. Mostrar información de los grupos")
    print("8. Registrar notas de los modulos (Filtros)")
    print("9. Atras")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        system("clear")
        if opcion == '1':
            while True:
                menu_coordinadores()
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    FCRUD.agregar_camper()
                elif opcion == '2':
                    FCRUD.mostrar_info_campers()
                elif opcion == '3':
                    FCRUD.actualizar_campers()
                elif opcion == '4':
                    FCRUD.prueba_inicial()
                elif opcion == '5':
                    FCRUD3.crear_salon()
                elif opcion == '6':
                    FCRUD3.metercamper_salon()
                elif opcion == '7':
                    FCRUD3.mostrar_info_salones()
                elif opcion == '8':
                    FCRUD4.registrar_notas_filtros()        
                elif opcion == '9':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        elif opcion == '2':
            while True:
                menu_trainers()
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    FCRUD2.registrar_trainer()
                elif opcion == '2':
                    FCRUD2.mostrar_info_trainers()
                elif opcion == '3':
                    FCRUD2.jornada_trainer()
                elif opcion =='4':
                    FCRUD2.actualizar_trainers()         
                elif opcion == '5':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        elif opcion == '3':
            while True:
                menu_reportes()
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    RPT.Listar_Campers_Inscritos()
                elif opcion == '2':
                    RPT.Listar_Campers_Aprobados()
                elif opcion == '3':
                    RPT.entrenadores_en_campuslands()
                elif opcion =='4':
                    RPT.campers_bajo_rendimiento()
                elif opcion =='5':
                    RPT.campers_y_trainers_asociados()
                elif opcion =='6':
                    RPT.superaron_y_no_superaron_60()                 
                elif opcion == '7':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")    
        elif opcion == '4':
            print("¡Hasta luego usuario! ")
            break    
        else:
            print("la opcion ingresada no es válida, por favor ingresa una de las opciones disponibles. ")     

if __name__ == "__main__":
    main()
 