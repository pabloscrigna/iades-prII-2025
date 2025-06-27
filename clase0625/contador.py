from collections import Counter

lista_numeros = [4, 6, 7, 8, 9, 9, 4]


numeros_counter = Counter(lista_numeros)

print(numeros_counter)


frase = ["a", "e", "i", "o", "e", "i"]

letra_counter = Counter(frase)

print(letra_counter)
print(letra_counter["e"])
print(letra_counter.most_common(2))
print(letra_counter.items())