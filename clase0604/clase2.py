"""
Las clases tiene atributos. Podemos distinguir dos tipos de atributos

Atributos de instancia: Pertenecen a la instancia de la clase o al objeto. 
Son atributos particulares de cada instancia


Atributos de clase: Se trata de atributos que pertenecen a la clase, 
por lo tanto van a ser comunes para todos los objetos

"""

# Definimos la clase con  3 atributos de instancia
# nombre - edad - altura
class Persona:

    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura


# inicializamos dos objetos de la clase Persona
p1 = Persona("Ruben", 36, 1.98)
p2 = Persona("Marisa", 24, 1.55)

# como acceder a los atributos

print("el objeto p1 tiene los atributos:")
print(f"nombre: {p1.nombre} -- edad: {p1.edad} -- altura: {p1.altura}")

print("el objeto p2 tiene los atributos:")
print(f"nombre: {p2.nombre} -- edad: {p2.edad} -- altura: {p2.altura}")


if p1.edad > p2.edad:
    print(f"{p1.nombre} es mayor que {p2.nombre}")


# self : es una variable que representa la instancia de la clase 



# Atributos de  clase

class Alumno:

    # Atributo de clase
    clave = 2509

    def __init__(self, nombre, curso, activo):
        self.nombre = nombre
        self.curso = curso
        self.activo = activo

alumno1 = Alumno("Raul", "noche", False)
alumno2 = Alumno("Woody Vaquero", "tarde", True)

print(f"nombre: {alumno1.nombre} -- curso: {alumno1.curso} -- activo: {alumno1.activo}")
print(f" alumno clave: {alumno1.clave}")

print(f"clase alumno clave: {Alumno.clave}")









