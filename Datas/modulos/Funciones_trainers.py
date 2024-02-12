import json

def registrar_trainer():
    with open("Datas/Trainers.json", "r") as outfile:
        Data = json.load(outfile)


    nuevo_trainer = {}
    nuevo_trainer["ID"] = int(input("Ingrese el ID del nuevo trainer: "))
    nuevo_trainer["N_documento"] = int(input("Ingrese el numero de documento del nuevo trainer: "))
    nuevo_trainer["nombre"] = input("Ingrese el primer nombre del nuevo trainer: ")
    nuevo_trainer["apellido"] = input("Ingrese el primer apellido del nuevo trainer: ")
    nuevo_trainer["N_celular"] = input("Ingrese el numero de celular del nuevo trainer: ")

    Data["trainers"].append(nuevo_trainer)

    with open("Datas/trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)