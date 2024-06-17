import pickle
import os
import random

def crear_ticket():
    datos = {
        "Nombre": input("Ingrese su nombre: "),
        "Sector": input("Ingrese su sector: "),
        "Asunto": input("Ingrese Asunto: "),
        "Mensaje": input("Ingrese su mensaje: "),
        "Ticket": random.randrange(1000, 9999)
    }

    print("=============================")
    print("Se generó el siguiente ticket")
    print("=============================")
    for key, value in datos.items():
        print(f"{key}: {value}")
    print("=============================")
    print("=============================")

    guardar = f"ticket_{datos['Ticket']}.pickle"
    with open(guardar, "wb") as f:
        pickle.dump(datos, f)
    print(f"El ticket se ha guardado en el archivo: {guardar}. Recuerde su número de ticket por favor")


def leer_ticket():
    numero_ticket = input("Ingrese el número de ticket: ")
    archivo = f"ticket_{numero_ticket}.pickle"
    if os.path.isfile(archivo):
        with open(archivo, "rb") as f:
            ticket = pickle.load(f)
            print("Datos del ticket:")
            print("=============================")
            print("=============================")    
            for key, value in ticket.items():
                print(f"{key}: {value}")
            print("=============================")
            print("=============================")    
    else:
        print("El ticket no existe.")

def main():
    print("Hola, bienvenidos al sistema de tickets")
    while True:
        print("1 - Crear un nuevo ticket")
        print("2 - Leer un ticket")
        print("3 - Salir")
        opcion = input("Seleccione: ")
        if opcion == "1":
            crear_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            print("Fin del programa")
            break
        else:
            print("Opción inválida")

main()