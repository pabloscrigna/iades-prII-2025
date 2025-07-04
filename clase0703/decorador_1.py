
def saludar(nombre, logger):
    logger(f"Hola, {nombre}")

# metodo para girar un string
def rotacion(frase):
    print(frase[::-1])


saludar("Alan", rotacion)

