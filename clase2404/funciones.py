"""
Que es una funcion?

Codigo mas ordenado
agrupar codigo

"""

# Funciones incorporadas en python
# funcion print
print("Hola mundo!!")

# funcion input
dato = input("")

# funcion len
len([0,2,3])


# ¿como definimos una funcion?

# def nombre_de_la_funcion(parametros):
#     Codigo de la funcion
#     return expresion


def saludar_nombre(nombre):
    print(f"hola {nombre}")
    

def sumar(a,b):
    return a + b

resultado = sumar(1,2)
print("resultado: ",resultado)

print("solo invocar sumar")
sumar(6,7)

resultado = saludar_nombre("Raul")

print("return saludar ", resultado)

