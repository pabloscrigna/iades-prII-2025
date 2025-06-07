

# Definimos la clase calculadora
# 2 atributos de instancia: numero1 y numero2
# 2 metodos: suma y multiplicar   
class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def multiplicar(self):
        return self.numero1 * self.numero2

    def suma(self):
        return self.numero1 + self.numero2

    @property
    def resta(self):
        return self.numero1 - self.numero2

calc = Calculadora(10, 5)
foo = Calculadora(20,5, 3)

print(f"valores: {calc.numero1} -- {calc.numero2}")


print("resultado multiplicacion: ", calc.multiplicar())
print("resultado suma: ", calc.suma())

print("resultado resta: ", calc.resta)
print("resultado resta: ", foo.resta)