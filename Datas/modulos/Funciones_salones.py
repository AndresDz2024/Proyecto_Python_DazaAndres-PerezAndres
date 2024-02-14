import json
from os import system
def menu_rutas():
    print("\nRutas disponibles:")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    opcion = input("Seleccione el número correspondiente a la ruta a asignar: ")
    system("clear")

    if opcion == '1':
        return "NodeJS"
    elif opcion == '2':
        return "Java"
    elif opcion == '3':
        return "NetCore"
    else:
        print("Ingrese una opción válida")
        return menu_rutas()

def menu_areas():
    print("\nAreas de entrenamiento disponibles: ")
    print("1. Sputnik")
    print("2. Artemis")
    print("3. Apolo")
    opcion = input("Seleccione el area de entrenamiento: ")
    system("clear")

    if opcion == '1':
        return "Sputnik"
    elif opcion == '2':
        return "Artemis"
    elif opcion == '3':
        return "Apolo"
    else:
        print("Ingrese una opción válida")
        return menu_areas()

def Crear_salon():
    with open("Datas/Salones.json", "r") as file:
        data = json.load(file)

    nuevo_salon = {}
    ultimo_id = max([salon["Id"] for salon in data["Salones"]], default=0) + 1
    nuevo_salon["Id"] = ultimo_id
    nuevo_salon["nombre del grupo"] = input("Ingrese el nombre del salón: ")

    with open("Datas/Trainers.json", "r") as file:
        trainers_data = json.load(file)["Trainers"]

    while True:
        try:
            id_trainer = int(input("Ingrese el ID del Trainer que se encargará de este salón: "))
            for trainer in trainers_data:
                if trainer["ID"] == id_trainer:
                    nuevo_salon["Trainer_encargado"] = trainer["nombre"]
                    nuevo_salon["Horario_de_grupo"] = trainer["Horario"]
                    break
            else:
                print("El ID del Trainer no existe. Por favor, ingrese un ID válido.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico.")

    nuevo_salon["Ruta"] = menu_rutas()
    nuevo_salon["Salon"] = menu_areas()
    data["Salones"].append(nuevo_salon)

    with open("Datas/Salones.json", "w") as file:
        json.dump(data, file, indent=4)


# def crear_salon():
#     with open("Datas/Salones.json", "r") as file:
#         data = json.load(file)

#     nuevo_salon = {}
#     ultimo_id = max([salon["Id"] for salon in data["Salones"]], default=0) + 1
#     nuevo_salon["Id"] = ultimo_id
#     nuevo_salon["nombre del grupo"] = input("Ingrese el nombre del salón: ")

#     with open("Datas/Trainers.json", "r") as file:
#         trainers_data = json.load(file)["Trainers"]

#     while True:
#         try:
#             id_trainer = int(input("Ingrese el ID del Trainer que se encargará de este salón: "))
#             for trainer in trainers_data:
#                 if trainer["ID"] == id_trainer:
#                     for salon_existente in data["Salones"]:
#                         if salon_existente["Trainer_encargado"] == trainer["nombre"] and salon_existente["Horario_de_grupo"] == trainer["Horario"]:
#                             print("El entrenador ya tiene un grupo en este horio.")
#                             break
#                     else:
#                         nuevo_salon["Trainer_encargado"] = trainer["nombre"]
#                         nuevo_salon["Horario_de_grupo"] = trainer["Horario"]
#                         break
#             else:
#                 print("El ID del Trainer no existe. Por favor, ingrese un ID válido.")
#                 continue
#             break
#         except ValueError:
#             print("Por favor, ingrese un valor numérico.")

#     nuevo_salon["Ruta"] = menu_rutas()
#     nuevo_salon["Salon"] = menu_areas()
#     data["Salones"].append(nuevo_salon)

#     with open("Datas/Salones.json", "w") as file:
#         json.dump(data, file, indent=4)
