"""
Metodos Especiales

Voy a hacer una clase vector que almacena un punto x, y en una lista
"""

class Vector():

    def __init__(self, datos):
        self.datos = datos
        self.factor = sum(datos)


if __name__ == "__main__":
    v1 = Vector([3, 4])
    
    print(f"datos : {v1.datos}")
    print(f"x: ")

