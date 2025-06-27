from collections import Counter

direcciones = Counter([
    linea.split()[0]
    for linea in open("mini-access-log.txt")
])

# print(direcciones)
print(direcciones.most_common(4))