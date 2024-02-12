import json

def agregar_camper():
    with open("Datas/Campers.json", "r") as outfile:
        Data = json.load(outfile)


    nuevo_camper = {}
    nuevo_camper["ID"] = int(input("Ingrese el ID del nuevo camper: "))
    nuevo_camper["N_documento"] = int(input("Ingrese el numero de documento del nuevo camper: "))
    nuevo_camper["nombre"] = input("Ingrese el primer nombre del nuevo camper: ")
    nuevo_camper["nombre2"] = input("Ingrese el segundo nombre del nuevo camper: ")
    nuevo_camper["apellido"] = input("Ingrese el primer apellido del nuevo camper: ")
    nuevo_camper["apellido2"] = input("Ingrese el segundo apellido del nuevo camper: ")
    nuevo_camper["ciudad"] = input("Ingrese la ciudad del nuevo camper: ")
    nuevo_camper["Direccion"] = input("Ingrese la Dirección del nuevo camper: ")
    nuevo_camper["Acudiente"] = input("Ingrese El nombre del acudiente del nuevo camper: ")
    nuevo_camper["N_celular"] = input("Ingrese el numero de celular del nuevo camper: ")
    nuevo_camper["N_fijo"] = input("Ingrese el numero de teléfono fijo del nuevo camper: ")
    nuevo_camper["Estado"] = "Inscrito"

    Data["Campers"].append(nuevo_camper)

    with open("Datas/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def mostrar_info_campers():
    with open("Datas/Campers.json", "r") as outfile:
        Data = json.load(outfile)

        campers = Data["Campers"]

        ID_camper = int(input("Ingresa el id del Camper del que quieras ver la información: "))
        print("\n")

        for camper in campers: 
            if camper["ID"] == ID_camper:
                for key, value in camper.items():
                    print(f"{key}: {value}")
                print("\n")
                        
                        

def actualizar_campers():
    editacion = open("Datas/Campers.json")
    Data = json.load(editacion)
    campers = Data["Campers"]
    ID_camper = int(input("Ingresa el id del Camper que quieras actualizar: "))
    for camper in campers:
        if camper["ID"] == ID_camper:
            
            N_documento = input("Ingresa el nuevo numero de documento: ")
            nombre = input("Ingresa el nuevo primer nombre: ") 
            nombre2 = input("Ingresa el nuevo segundo nombre: ")
            apellido = input("Ingresa el nuevo apellido: ")
            apellido2 = input("Ingresa el nuevo segundo apellido: ")
            ciudad = input("Ingresa la nueva ciudad: ")
            Direccion = input("Ingrese la nueva direccion: ")
            Acudiente = input("Ingresa el nuevo nombre del acudiente: ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            N_fijo = input("Ingresa el nuevo numero de teléfono fijo: ")
            
            camper["N_documento"] = N_documento
            camper["nombre"] = nombre
            camper["nombre2"] = nombre2
            camper["apellido"] = apellido
            camper["apellido2"] = apellido2 
            camper["ciudad"] = ciudad
            camper["Direccion"] = Direccion
            camper["Acudiente"] = Acudiente
            camper["N_celular"] = N_celular
            camper["N_fijo"] = N_fijo
            
    
    with open("Datas/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def prueba_inicial():
    with open("Datas/Campers.json", "r") as outfile:
        Data = json.load(outfile)
        campers = Data["Campers"]

    while True:
        ID_camper = int(input("Ingresa el id del Camper del cual deseas ingresar la nota de su prueba inicial: "))
        for camper in campers:
            if camper["ID"] == ID_camper:
                while True:
                    nota_practica = int(input("Ingrese la nota practica de la prueba de inicial: "))
                    if 0 <= nota_practica <= 100:
                        while True:
                            nota_teorica = int(input("Ingrese la nota teorica de la prueba de inicial: "))
                            if 0 <= nota_teorica <= 100:
                                while True:
                                    nota_ingreso = nota_practica + nota_teorica/2
                                    if nota_ingreso >= 60:
                                        camper["Estado"] = "En proceso de ingreso"
                                        break
                                    else:
                                        camper["Estado"] = "Reprobado"
                                        break
                                break
                            else:
                                print("Nota no valida, ingresa un valor de 0 a 100")
                        break
                    else:    
                        print("Nota no valida, ingresa un valor de 0 a 100")
                break        
        break                     

    with open("Datas/Campers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

                        