
def saludar(nombre, logger):
    logger(f"Hola, {nombre}")


logger = print


saludar("Martin", logger)




import logging


logging.error("Ocurrio un error")

saludar("Mica", logging.error)

with open("data.txt", "w") as file:
    nombre = "Pablo"
    file.write(f"Hola!!!, {nombre}")
    saludar("Juan", file.write)


# metodo para girar un string
def rotacion(frase):
    print(frase[::-1])


s = "Hola mundo"

rotacion(s)

