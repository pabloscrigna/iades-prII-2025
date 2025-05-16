"""
Lectura de un archivo 

funcion: readline

"""

# Abre el archivo en modo lectura en modo texto
file = open("data", "r")

# lee la primera linea y la almacena en linea
# type(linea) ---> str 
linea = file.readline()

# mientras el archivo tenga lineas para leer leemos
while linea:
    linea = linea.strip()
    print(f"linea: {linea}  -- largo linea: {len(linea)}")
    linea = file.readline()


print(f"linea final: {linea}  -- largo linea final: {len(linea)}")

# cerramos el archivo
file.close()