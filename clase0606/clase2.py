class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    
    def calcular_superficie(self):
        return self.lado * 2


figura = Cuadrado(10)
figura2 = Cuadrado(20)

print("figura", figura)

superficie = figura.calcular_superficie()

print("Superficie del cuadrado", superficie)