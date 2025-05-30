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
#     "fecha_modificacion": "2023-01-01"
# }


# Menu 1. Ingresar repuesto
#      2. Editar
#      3. Listar
#      4. Buscar  
#      5. Eliminar
#      6. Salir

import json

from abm import (
    ingresar_repuesto,
    editar_repuesto,
    buscar_repuesto,
    listar_repuestos,
)
from config import REPUESTOS_FILE
from utils import guardar


def mostrar_menu():
    print("""
     1. Ingresar repuesto
     2: Editar 
     3: Listar
     4: Buscar
     5: Eliminar
     6: Salir

     7: Guardar
    """)

    return

def main():
    with open(REPUESTOS_FILE, "r") as file:
        repuestos = json.load(file)

    while(True):

        print("repuestos: ", repuestos)

        mostrar_menu()

        opcion = input("Ingresar una opcion: ")

        match opcion:

            case "1":
                print("Ingresar repuesto")
                repuesto = ingresar_repuesto()
                repuestos.append(repuesto)

            case "2":
                codigo = input("Ingrese el codigo a editar: ")
                respuesta = editar_repuesto(codigo, repuestos)
                if respuesta:
                    print("edicion exitosa")

            case "3":
                listar_repuestos(repuestos)

            case "4":
                codigo = input("Ingrese el codigo a buscar: ")
                repuesto = buscar_repuesto(codigo, repuestos)
                print("repuesto: ", repuesto)    
                
            case "5":
                eliminar_repuesto()

            case "6":
                break

            case "7":        
                guardar(REPUESTOS_FILE, repuestos)


if __name__ == "__main__":
    main()
