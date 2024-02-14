import json
from os import system

def registrar_trainer():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)


    nuevo_trainer = {}
    ultimo_id = max([trainer["ID"] for trainer in Data["Trainers"]], default=0)
    nuevo_id = ultimo_id + 1
    nuevo_trainer["ID"] = nuevo_id
    nuevo_trainer["N_documento"] = input("Ingrese el numero de documento del nuevo trainer: ")
    nuevo_trainer["nombre"] = input("Ingrese el primer nombre del nuevo trainer: ")
    nuevo_trainer["apellido"] = input("Ingrese el primer apellido del nuevo trainer: ")
    nuevo_trainer["N_celular"] = input("Ingrese el numero de celular del nuevo trainer: ")
    nuevo_trainer["Jornada"] = "No asignado"

    Data["Trainers"].append(nuevo_trainer)

    with open("Datas/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def mostrar_info_trainers():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)

        trainers = Data["Trainers"]
        while True:
            try:
                ID_trainer = int(input("Ingresa el id del Trainer del que quieras ver la información: "))
                print("\n")

                for trainer in trainers: 
                    if trainer["ID"] == ID_trainer:
                        for key, value in trainer.items():
                            print(f"{key}: {value}")
                        print("\n")    
            except ValueError:
                print("\nPor favor ingrese un  valor numerico")            
            break    
        
# def horario_trainer():
#     with open("Datas/Trainers.json", "r") as outfile:
#         Data = json.load(outfile)

#         trainers = Data["Trainers"]
#     while True:
#         try:
#             ID_trainer = int(input("ingrese el ID del trainer al cual desea asignarle un horario: "))
#             for trainer in trainers:

#                 if trainer["ID"] == ID_trainer:
                    
#                     print("\nHorarios:")
#                     print("1. 6:00 a.m - 10:00 a.m")
#                     print("2. 10:00 a.m - 2:00 p.m")
#                     print("3. 2:00 p.m - 6:00 p.m")
#                     print("4. 6:00 p.m - 10:00 p.m")
                    
#                     opcion = input("Seleccione el horario a asignar: ")
#                     system("clear")

                    
#                     if opcion == '1':
#                         horario = "6:00 a.m - 10:00 a.m"
#                         trainer["Horario"] = horario
                        
#                     elif opcion == '2':
#                         horario = "10:00 a.m - 2:00 p.m"
#                         trainer["Horario"] = horario  
                        
#                     elif opcion == '3':
#                         horario = "2:00 p.m - 6:00 p.m"
#                         trainer["Horario"] = horario
                        
#                     elif opcion == '4':
#                         horario = "6:00 p.m - 10:00 p.m"
#                         trainer["Horario"] = horario
#                     else:
#                         print("Ingrese una opcion válida ")
#         except ValueError:
#             print("\nIngresa un valor numerico ")                     
#         break            

#     with open("Datas/Trainers.json", "w") as outfile:
#         json.dump(Data, outfile, indent=4)                


def jornada_trainer():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)

    trainers = Data["Trainers"]
    while True:
        try:
            ID_trainer = int(input("Ingrese el ID del trainer al cual desea asignarle un horario: "))
            for trainer in trainers:
                if trainer["ID"] == ID_trainer:
                    print("\nJornadas:")
                    print("1. Mañana (6:00 a.m - 2:00 p.m)")
                    print("2. Tarde (2:00 p.m - 10:00 p.m)")
                    
                    opcion = input("Seleccione la jornada que desea asignar: ")
                    system("clear")

                    if opcion == '1':
                        jornada = "Mañana"
                        trainer["Jornada"] = jornada
                    elif opcion == '2':
                        jornada = "Tarde"
                        trainer["Jornada"] = horario
                    else:
                        print("Ingrese una opción válida")
        except ValueError:
            print("\nIngrese un valor numérico")
        break

    with open("Datas/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def actualizar_trainers():
    editacion = open("Datas/Trainers.json")
    Data = json.load(editacion)
    trainers = Data["Trainers"]
    ID_trainer = int(input("Ingresa el id del trainer que quieras actualizar: "))
    for trainer in trainers:
        if trainer["ID"] == ID_trainer:
            
            N_documento = input("Ingresa el nuevo numero de documento: ")
            nombre = input("Ingresa el nuevo primer nombre: ") 
            apellido = input("Ingresa el nuevo apellido: ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            
            trainer["N_documento"] = N_documento
            trainer["nombre"] = nombre
            trainer["apellido"] = apellido
            trainer["N_celular"] = N_celular
    
    with open("Datas/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)        


        
        

    
