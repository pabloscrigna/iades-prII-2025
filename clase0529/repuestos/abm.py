from datetime import datetime, timezone

from config import MAX_REPUESTOS

def ingresar_repuesto():
    """
    docstring
    """
    repuesto = {}

    repuesto["nombre"] = input("ingrese el nombre del repuesto: ")
    repuesto["codigo"] = input("ingrese el codigo: ")
    repuesto["fecha_ingreso"] = datetime.now(timezone.utc).isoformat()  
    repuesto["fecha_modificacion"] = datetime.now(timezone.utc).isoformat()
    
    return repuesto

def buscar_repuesto(codigo, repuestos):
    
    for repuesto in repuestos:
        cod = repuesto.get("codigo", "")
        if codigo == cod:
            return repuesto

    return        


def editar_repuesto(codigo, repuestos):
    """
    docstring
    """

    for repuesto in repuestos:
        if repuesto["codigo"] == codigo:
            repuesto["nombre"] = input("ingrese el nuevo nombre: ")
            repuesto["fecha_modificacion"] = datetime.now(timezone.utc).isoformat()

            return repuesto 

    return

def listar_repuestos(repuestos):
    contador = 0

    for repuesto in repuestos:
        codigo = repuesto["codigo"]
        nombre = repuesto["nombre"]

        print("----------")
        print(f"codigo: {codigo}  nombre: {nombre}")

        contador +=1    
        if contador == MAX_REPUESTOS:
            input()