"""
Dada una lista de entreros del 0 - 100
Generar una nueva list con los valores pares
"""

# numeros = []
# 
# for i in range(1,101):
#     numeros.append(i)

numeros = list(range(1,101))


lista_pares = [
    i
    for i in numeros
    if i % 2 == 0
]


print(lista_pares)