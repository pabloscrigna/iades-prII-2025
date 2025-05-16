"""
Modo de apertura de archivos
Abrir un archivo

open()

"""
# Modo texto
# Abrimos el archivo para lectura
try:
    archivo = open("datas","r")
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe")


# Abrimos el archivo para escribir
archivo = open("datos", "w")
archivo.close()


# Abrir el archivo para agregar informacion
fp = open("data_a", "a")
fp.close()






