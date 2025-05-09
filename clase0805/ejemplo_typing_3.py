from typing import Union

frutas_cocina = {
    "bananas" : 7,
    "peras" : 12.8,
    "manzanas" : 7
}


def contar_frutas(frutas: dict[str, int | float])-> int | float:
    
    contador = 0.0

    for cantidad in frutas.values():
        contador += cantidad

    return contador



cantidad_frutas = contar_frutas(frutas_cocina)

print("la cantidad de frutas es: ", cantidad_frutas)





