"""
Hacer un programa que lea un archivo y
lo guarde en otro archivo sin lineas vacias

el el nombre del archivo destino es el nombre del archivo origen + "_sn"


"""

# abrir en modo r
archivo_input = "demo.txt"
# abrir en modo w
archivo_output = f"{archivo_input}_sn"

file_input = open(archivo_input, "r")
file_output = open(archivo_output, "w")

condicion = True

while condicion:
    condicion = False
    linea = file_input.readline()

    if linea != "\n" and linea:
        # escribirla en el archivo
        file_output.write(linea)

    if linea:
        condicion = True        

file_input.close()
file_output.close()
    