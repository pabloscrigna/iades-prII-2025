# Hacer una lista con el archivo shoe-data.txt, y cada linea sea un diccionario
# Hacer una funcion que le pasamos la linea y arme el diccionario

shoes = [] 

def linea_a_diccionario(linea: str) -> dict:
    # print(linea.strip().split("\t"))
    # campos = linea.strip().split("\t")
    # return {
    #     "marca": campos[0],
    #     "color": campos[1],
    #     "talle": campos[2]
    # }
    # unpacking
    marca, color, talle = linea.strip().split("\t")
    return {
        "marca": marca,
        "color": color,
        "talle": talle
    }


with open("shoe-data.txt", "r") as file:
    for linea in file:
        shoes.append(linea_a_diccionario(linea))

print(shoes)