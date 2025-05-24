"""
ejercicio integrador
"""


"""
Inventario de repuestos
"""



# respuesto = {
#     "nombre": "Tornillo",
#     "codigo": 123456,
#     "precio": 0.50,
#     "cantidad": 100,
#     "proveedor": {
#         "nombre": "Proveedor 1",
#         "telefono": "123456789",
#         "direccion": "Calle Falsa 123"
#     },
#     "categoria": "Herramientas",
#     "fecha_ingreso": "2023-01-01"
# }


# Menu 1. Ingresar repuesto
#      2. Editar
#      3. Listar
#      4. Buscar  
#      5. Eliminar
#      6. Salir

import json

REPUESTOS_FILE = "repuestos.json"

def mostrar_menu():
    pass

def ingresar_repuesto():

    repuesto = {}

    repuesto["nombre"] = input("ingrese el nombre del repuesto: ")
    repuesto["codigo"] = input("ingrese el codigo: ")

    return repuesto

def editar_repuesto():

    codigo = input("ingresar el codigo del respuesto a editar: ")

    for repuesto in repuestos:
        if repuesto["codigo"] == codigo:
            repuesto["nombre"] = input("ingrese el nuevo nombre: ")

    return

def guardar():

    with open(REPUESTOS_FILE, "w") as file:
        json.dump(repuestos,file,indent=4)


with open(REPUESTOS_FILE, "r") as file:
    repuestos = json.load(file)

# print("repuestos: ", repuestos)

while(True):

    print("repuestos: ", repuestos)

    mostrar_menu()
    
    opcion = input("Ingresar una opcion")

    match opcion:

        case "1":
            print("Ingresar repuesto")
            repuesto = ingresar_repuesto()
            repuestos.append(repuesto)

        case "2":
            editar_repuesto()

        case "3":
            listar_repuesto()

        case "4":
            buscar_repuesto()

        case "5":
            eliminar_repuesto()

        case "6":
            break

        case "7":        
            guardar()