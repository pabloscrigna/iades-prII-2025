class Potencia:

    def __init__(self, exponente):
        self.exponente = exponente

    # def operacion(self,numero):
    def __call__(self, numero):
        resultado = numero ** self.exponente
        return resultado

potencia_dos = Potencia(2)

# print(f"resultado: ", potencia_dos.operacion(5))

print(f"resultado: ", potencia_dos(5))

potencia_tres = Potencia(3)

print("resultado : ", potencia_tres(3))