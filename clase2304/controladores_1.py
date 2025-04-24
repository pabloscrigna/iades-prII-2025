"""
if    if/else    if/elif/else   ---->  condicionales    
"""

"""
whle / for  ----> iterativos 
"""

edad = 30

# el if evalua un condicional ---> True / False

if edad > 18:
    print("es mayor de edad")

# >  mayor
# < menor
# >= mayor igual
# <= menor igual
# != no igual


if edad > 20:
    print("es mayor de 20")
elif edad > 18:
    print("es mayor de 18")
else:
    print("Es menor de edad")


if edad > 18:
    print("es mayor de 18")
    if edad > 20:
        print("es mayor de 20")

print("ejemplo lista")

lista = [2, 4]     # la lista vacia se evalua como False


if lista:
    valor = lista.pop()
    print("valor :", valor)
    print("lista :", lista)
else:
    print("No hay mas elementos en la lista")

print("FIN")


frase = ""    # se evalua tambien como false
numero = 0    # se evalua como false
condicion = False  # se evalua como False

