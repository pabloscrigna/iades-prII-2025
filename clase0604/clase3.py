"""
Clases:

Atributos: Instancia y de Clase 

Metodos
"""

class Rectangulo:

    def __init__(self, lado_a, lado_b):
        self.ladoA = lado_a
        self.ladoB = lado_b

    def superficie(self):
        resultado = self.ladoA * self.ladoB
        return resultado

    def perimetro(self):
        resultado = 2 * (self.ladoA + self.ladoB)
        return resultado    

figura1 = Rectangulo(10, 5)
figura2 = Rectangulo(20,7)

print(f"lado A: {figura1.ladoA} lado B: {figura1.ladoB}")

print(f"superficie rectangulo: {figura1.superficie()}")
print(f"perimetro rectangulo: {figura1.perimetro()}")
    

