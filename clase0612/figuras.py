class Rectangulo:

    def __init__(self, base, altura):
      print("Ejecutando metodo init de rectangulo")
      self.base = base
      self.altura = altura  

    def area(self):
        print("Ejecutando area rectangulo....")
        return self.base * self.altura

    def perimetro(self):
        print("Ejecutando perimetro Rectangulo...")
        return self.base * 2 + self.altura * 2

""""
Clase Cuadrado que hereda de la clase Rectangulo
Atributos:
    base: Heredada de Rectangulo
    altura: Heredada de Rectangulo
    lado: de la clase cuadrado

Metodos:
    Constructor: metodo init de cuadrado y llamamos al init de Rectangulo
    perimetro: llamamos al metodo periemetro de la clase padre
    area: heredado de la clase padre (Rectangulo)
"""
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        print("Ejecutando metodo init de cuadrado...")
        self.lado = lado
        # llamamos al metodo init de la clase padre (Rectangulo)
        super().__init__(lado, lado)

    def perimetro(self):
        print("Ejecutando perimetro de cuadrado")
        # llamamos al metodo perimetro de la clase padre
        valor_perimetro = super().perimetro()
        return valor_perimetro


# Rectangulo
# rectangulo = Rectangulo(10,7)
# area_rectangulo = rectangulo.area()
# perimetro_rectangulo = rectangulo.perimetro() 
# print("Area rectangulo: ", area_rectangulo)
# print("Perimetro rectangulo: ", perimetro_rectangulo)


# Cuadrado    
cuadrado = Cuadrado(5)
print(f"lado: {cuadrado.lado} -- base: {cuadrado.base} -- altura: {cuadrado.altura}")

area_cuadrado = cuadrado.area()
print("area cuadrado: ", area_cuadrado)
perimetro_cuadrado = cuadrado.perimetro()
print("perimetro cuadrado: ", perimetro_cuadrado)