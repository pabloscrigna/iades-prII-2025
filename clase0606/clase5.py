class Calculadora:

    def __init__(self, *args):
        self.numeros = args

    def suma(self):
        resultado = 0

        for numero in self.numeros:
            resultado += numero
        return resultado


    def version(self):
        return "Version Calculadora 7"

    @staticmethod
    def version_1():
        return "Version Calculadora 7 - estatico"


foo = Calculadora(6,7,8,9)


print("resultado: ", foo.suma())


foo = Calculadora(1,3)
print("resultado: ", foo.suma())


print(foo.version())

print(Calculadora.version_1())