import json

def Crear_C():
    with open("Campers.json", "r") as outfile:
        Data = json.load(outfile)

    nuevo_camper = {}
    
    nuevo_camper["N_documento"] = int(input("Ingrese el ID del nuevo camper: "))
    nuevo_camper["nombre"] = input("Ingrese el primer nombre del nuevo camper: ")
    nuevo_camper["nombre2"] = input("Ingrese el segundo nombre del nuevo camper: ")
    nuevo_camper["apellido"] = input("Ingrese el primer apellido del nuevo camper: ")
    nuevo_camper["apellido2"] = input("Ingrese el segundo apellido del nuevo camper: ")
    nuevo_camper["ciudad"] = input("Ingrese la ciudad del nuevo camper: ")
    nuevo_camper["Direccion"] = input("Ingrese la Dirección del nuevo camper: ")
    nuevo_camper["Acudiente"] = input("Ingrese El nombre del acudiente del nuevo camper: ")
    nuevo_camper["N_celular"] = input("Ingrese el numero de celular del nuevo camper: ")
    nuevo_camper["N_fijo"] = input("Ingrese el numero de teléfono fijo del nuevo camper: ")
    nuevo_camper["Estado"] = "En proceso de ingreso"

    Data["Campers"].append(nuevo_camper)

    with open("Campers.json", "w") as outfile:
        json.dump(Data, outfile,indent=4)
        


def Leer_C():

    with open("Campers.json") as outfile:
        Data = json.load(outfile)

        campers = Data["Campers"]
        campers_ordenados = sorted(campers, key=lambda x: x["Acudiente"])
        for i in campers_ordenados:
            for key, value in i.items():
                print(f"{key}: {value}")
            print("\n")