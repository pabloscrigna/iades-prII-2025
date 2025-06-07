class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    @property
    def calcular_superficie(self):
        return self.lado * 2

    @property
    def perimetro(self):
        return self.lado * 4

    def __str__(self):
        return f"Cuadrado de lado: {self.lado}"

figura = Cuadrado(10)
figura2 = Cuadrado(20)

print("figura", figura)

superficie = figura.calcular_superficie

print("Superficie del cuadrado", superficie)

perimetro = figura.perimetro

print("perimetro: ", perimetro)
