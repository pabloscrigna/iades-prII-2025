"""

Funciones de repaso


"""


lista = []           # creamos una lista vacia
diccionario = {}     # creamos un diccionario vacio


datos_prueba = [ '56 dominio1.com.ar', '23 dominio1.com.uy']

"""
dominio1.com.ar : 56
com.ar : 56
ar : 56
dominio1.com.uy : 23
com.uy : 23
uy: 23
"""


# xx dominio   


frase = "hola mundo!!!"

# separa un string...por default separa por espacio
foo = frase.split()

print(foo)


# separar un string por un valor 

frase = "hoy.esta.nublado"

foo = frase.split(".")
print(foo)


# como sacar el primer elemento de una lista
foo.pop(0)

print(foo)


# tengo una lista, unir los elementos de la lista por el simbolo $ y formar un string

foo = ".".join(foo)

print(foo)

foo = foo.split(".")

foo.pop(0)

print(foo)


frase = "a e i o u i o u t y u o"

contador = {}

for letra in frase:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(contador)



lista_salida = []


"""
dominio1.com.ar : 56
com.ar : 56
ar : 56
dominio1.com.uy : 23
com.uy : 23
uy: 23
"""

for key, value in diccionario.items()
    lista_salida.append(f"{value} {key}")