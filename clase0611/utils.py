

def imprimir(nombre: str, apellido: str) -> str:
    mensaje = f"{nombre}, {apellido}"

    print("Bienvenidos a la funcion!!!")
    print(mensaje)
    print(f"{nombre}, {apellido}")

    return f"{nombre}, {apellido}"
    # return



nombre = "juan"
apellido = "perez"


foo = imprimir(nombre, apellido) 

print("foo: ", foo)


# Archicos


with open("datos.csv", "w") as file:
    file.write("mica,cuello,19,353535,fecja") 
