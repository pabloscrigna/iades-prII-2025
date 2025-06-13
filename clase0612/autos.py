class Vehiculo:

    def __init__(self, marca, modelo):
        print("metodo init de la clase vehiculo")
        self.marca = marca
        self.modelo = modelo
        self.marca_modelo = f"{marca}-{modelo}"

    def mover(self):
        print("Metodo mover de la clase vehiculo")


class Coche(Vehiculo):
    
    def __init__(self, marca, modelo, combustible):
        self.combustible = combustible
        super().__init__(marca, modelo)

    def avanzar(self):
        print("metodo mover de la clase coche")
        super().mover()

class Foo:
    pass

class Bicicleta(Vehiculo, Foo):

    def __init__(self, marca, modelo, tipo):
        self.tipo = tipo
        super().__init__(marca, modelo)




coche = Coche("VW", "Vento", "naftero")

print(f"marca: {coche.marca}  -- modelo: {coche.modelo} -- combustible: {coche.combustible}")

coche.avanzar()