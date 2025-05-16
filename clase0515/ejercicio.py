"""
A partir de la funcion readline --- implementar readlines
readline --> retorna un string 
readlines() --> retorna una lista 
"""


def leelineas(archivo)-> list[str]:
    """
    le pasamos el archivo y retorna
    """
    lista_lineas = []

    linea = archivo.readline()

    while linea:
        lista_lineas.append(linea)
        linea = archivo.readline()

    return lista_lineas


file = open("data", "r")

lineas = leelineas(file)

print(lineas)