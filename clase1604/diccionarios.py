"""
diccionarios
"""


# dict vacio

dato = {}

dato_1 = dict()

print(f"{type(dato)} --- {type(dato_1)}")


# clave - valor
# clave: "nombre" -- cualquier tipo de dato inmutable
# valor: cualquier dato  -- mutable / inmutable

print("id dato", id(dato))
print("dato:", dato)
# Raul   ----> se crea una nueva variable tambien de tipo dict
# dato = {
#      "nombre": "Juan"
# }

print("id dato", id(dato))
# print("dato:", dato)


# Mica

# ingresando valores al diccionario

dato["nombre"] = "Mica"
print("dato:", dato)


dato["edad"] = 45


# leyendo un diccionario - Opcion 1 la clave tiene que existir
print("Opcion 1")

nombre = dato["nombre"]
# altura = dato["altura"]

print("nombre: ", nombre )
# print("altura: ", altura)

#  leyendo un diccionario - Opcion 2  
print("Opcion 2")
nombre = dato.get("nombre")
altura = dato.get("altura")

print("nombre: ", nombre )
print("altura: ", altura)


#  leyendo un diccionario - Opcion 3
nombre = dato.get("nombre")
altura = dato.get("altura", 0)

print("nombre: ", nombre )
print("altura: ", altura)


# eliminando una clave -- nombre

del dato["nombre"]
print("dato: ", dato)


# Agregamos la clave "nombre"

dato["nombre"] = "Mica"


# Leer todas las claves - keys

claves = dato.keys()
print("claves: ", claves)

for clave in claves:
    print("clave: ", clave)

# leer todos los valores - values
valores = dato.values()
print("valores: ", valores)

for valor in valores:
    print("valor: ", valor)

# leer todos los pares clave valor - items
clave_valor = dato.items()
print("clave - valor: ", clave_valor)

for clave, valor in dato.items():   # tambien puede ser la variable clave_valor
    print("clave: ", clave)
    print("valor: ", valor)
    print(f"clave: {clave}   valor: {valor}")

# le voy a agregar una clavec notas

dato["notas"] = [ 6, 7, 10]


# Calcular el promedio de las notas 

sum_de_notas = 0
notas = dato["notas"]
cantidad_de_notas = len(dato["notas"]) 

for nota in notas:
    sum_de_notas += nota     

promedio = sum_de_notas / cantidad_de_notas

print("promedio: ", promedio)


# lista de diccionarios

datos = []


# un programa que pida ingresar el nombre y la edad y lo guarde en una lista  / 2 



