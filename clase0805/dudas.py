
# ejemplo de for con range
print("range")
for i in range(10):
    print(i)


# ejemplo de for con lista
lista = list(range(10))
print("lista: ", lista)

for objeto in lista:
    print(objeto)



# ejemplo de for con strings
frase = "Hola mundo!!!"
lista_letras = []
letras_unicas = []

for letra in frase:
    lista_letras.append(letra)

    if not (letra in letras_unicas):
        letras_unicas.append(letra)

print("letras: ", lista_letras)
print("letras unicas: ", letras_unicas)

# slicing [inicio:fin:paso]
frase = "Hoy es Jueves 8 de Mayo"

print("frase: ",frase)
print("frase dada vuelta: ",frase[::-1])

print("frase a partir del indice 2 hasta el final: ", frase[2:])
print("frase a partir del indice 2 hasta el indice 4: ", frase[2:5])
print("frase a partir del indice 2 hasta el indice 10 en pasos de 2: ", frase[2:11:2])
print("imprime la frase en pasos de 2: ", frase[::2])