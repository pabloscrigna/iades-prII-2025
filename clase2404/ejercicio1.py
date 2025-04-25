"""
Crear un diccionario con los datos de las personas

diccionario persona:
    * nombre: str
    * apellido: str
    * direccion: object
        -Calle
        -Numero
        -piso
        -CP

ingresar 5 valores -- estructuras de datos de las personas


direccion = {
    "calle": "belgrano",
    "numero": "345",
    "piso": "5"
}


persona = {
    "nombre" : "Juan",
    "apellido : "perez",
    "direccion" : {
        "calle": "belgrano",
        "numero": "345",
        "piso": "5"
    }    
} 

"""

# creamos dos variables del tipo dict
direccion = {}    
persona = {}

# ingrese nombre y apellido
nombre = input("Ingrese el nombre de la persona: ")
apellido = input("ingrese el apellido de la persona: ")

# ingrese su direccion y ya lo guardamos en el diccionario direccion
direccion["calle"] = input("Ingrese la calle: ")
direccion["numero"] = input("Ingrese el numero: ")
direccion["piso"] = input("Ingrese el piso: ")

# asignamos los datos al dicconario persona
persona["nombre"] = nombre  
persona["apellido"] = apellido
persona["direccion"] = direccion

# Creamos el diccionario persona
print("direccion: ", direccion)
print("persona: ", persona)


# partiendo de persona imprimir
# nombre
print(persona["nombre"])

# direccion
print(persona["direccion"])

direccion_persona = persona["direccion"]

# imprimir la calle
print(direccion_persona["calle"])

calle = persona["direccion"]["calle"]
print("calle: ", calle)


# metodo get: Obtener el valor de una clave

# nombre
nombre = persona.get("nombre")
print("nombre: ", nombre)

# direccion
direccion = persona.get("direccion")

# calle
calle = direccion.get("calle")


# Ver solo las claves 
for clave in persona.keys():
    print("clave: ", clave)

# ver values
for valor in persona.values():
    print("valores: ", valor)


# clave valor
for clave, valor in persona.items():
    print(f"clave: {clave} --- valor: {valor}")


# como saber si una clave esta en un diccionario
# como ver si la clave nombre esta en un diccionario

opcion = "nombre" in persona

if opcion:
    print("esta")
else:
    print("no esta")
