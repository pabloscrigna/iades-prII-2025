


numeros = [ 6, 7, 8, 8, 9, 6 , 7, 8, 9]

contador = 0

repetidos = []

for numero in numeros:
    if numero not in repetidos:
        contador += numero
        repetidos.append(numero)

print("contador", contador)
print("repetidos", repetidos)