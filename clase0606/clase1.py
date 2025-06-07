class Persona:

    def __init__(self, nombre, edad, peso, sexo):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.sexo = sexo


class Alumno:

    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso


class Circulo:

    def superficie(radio):
        return (3.14 * radio)**2

p1 = Persona("Juan", 34, 56.8, "M")

a1 = Alumno("Mica", "Python")

print(f"{p1.nombre} -- {p1.edad}")
print(a1.nombre)

print(Circulo.superficie(2))



