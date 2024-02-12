import json

def registrar_trainer():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)


    nuevo_trainer = {}
    nuevo_trainer["ID"] = int(input("Ingrese el ID del nuevo camper: "))
    nuevo_trainer["N_documento"] = int(input("Ingrese el numero de documento del nuevo camper: "))
    nuevo_trainer["nombre"] = input("Ingrese el primer nombre del nuevo camper: ")
    nuevo_trainer["nombre2"] = input("Ingrese el segundo nombre del nuevo camper: ")
    nuevo_trainer["apellido"] = input("Ingrese el primer apellido del nuevo camper: ")
    nuevo_trainer["apellido2"] = input("Ingrese el segundo apellido del nuevo camper: ")
    nuevo_trainer["ciudad"] = input("Ingrese la ciudad del nuevo camper: ")
    nuevo_trainer["Direccion"] = input("Ingrese la Dirección del nuevo camper: ")
    nuevo_trainer["Acudiente"] = input("Ingrese El nombre del acudiente del nuevo camper: ")
    nuevo_trainer["N_celular"] = input("Ingrese el numero de celular del nuevo camper: ")
    nuevo_trainer["N_fijo"] = input("Ingrese el numero de teléfono fijo del nuevo camper: ")
    nuevo_trainer["Estado"] = "En proceso de ingreso"

    Data["Campers"].append(nuevo_trainer)

    with open("Datas/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)