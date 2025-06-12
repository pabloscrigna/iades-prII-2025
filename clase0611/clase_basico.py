from datetime import datetime

from persona import Persona

# generamos una instancia de la clase Persona
persona1 = Persona(nombre="pedro", apellido="sanchez", edad=49, dni="20456783")

print("Nombre: ", persona1.nombre)

print(persona1.datos())     # retorna un string: "<nombre>, <apellido> [<edad>]"

# generamos una nueva instancia de la clase Persona
persona2 = Persona("mica", "cuellos", 19, 678445456)


print(persona2.nombre)
print(persona2.apellido)
print(persona2.fecha)
print("tipo de dato de fecha: ", type(persona2.fecha))

persona2.apellido = "cuello"

print(persona2.nombre)
print(persona2.apellido)
print(persona2.fecha)


print(persona1.imprimir())
print(persona2.imprimir())


personas = []
personas.append(persona1)
personas.append(persona2)

persona = persona2

print(persona.nombre)


# personas = [persona1, persona2]
with open("datos.csv", "w") as file:
    # file.write(persona1.imprimir())
    # file.write(persona2.imprimir()) 

    for persona in personas:
        file.write(persona.imprimir())


print("Leyendo personas.....")

personas = []

with open("datos.csv", "r") as file:
    # metodos de lectura: read() - readline() - readlines()
    lineas = file.readlines()
    print(lineas)
    for linea in lineas :
        # linea = nombre,apellido,edad,dni.fecha  ---> str
        linea_lista = linea.split(",")
        print(linea_lista)

        nombre = linea_lista[0]
        apellido = linea_lista[1]
        edad = int(linea_lista[2])
        dni = int(linea_lista[3])
        fecha = datetime.strptime(linea_lista[4].replace("\n", ""), "%Y-%m-%d %H:%M:%S.%f")

        persona = Persona(nombre,apellido, edad, dni)    
        persona.fecha = fecha
        personas.append(persona)
        print("nombre: ", persona.nombre)
        print("fecha: ", persona.fecha)
        print("tipo de dato de fecha: ", type(persona.fecha))


print("personas: ", personas)
print(personas[0])
