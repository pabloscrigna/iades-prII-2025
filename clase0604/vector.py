"""
Metodos Especiales

Voy a hacer una clase vector que almacena un punto x, y en una lista
"""

class Vector():

    def __init__(self, datos):
        self.datos = datos
        self.dimensiones = len(datos)
        self.factor = sum(datos)

    def __str__(self):
        return f"Objeto del tipo Vector. sus valores son {self.datos}"

    def __len__(self):
        return self.dimensiones

    def __getitem__(self, indice):
        return self.datos[indice]

    def __setitem__(self, indice, valor):
        self.datos[indice] = valor

    def __iter__(self):
        for valor in self.datos:
            return valor

    def __add__(self):
        

if __name__ == "__main__":
    v1 = Vector([3, 4])
    
    print(f"datos : {v1.datos}")
