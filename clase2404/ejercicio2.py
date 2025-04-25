"""
uso de in
"""


lista = ["suma", "resta", "division"]


opcion = "suma" in lista      # in retorna True or False

print("opcion: ", opcion)


if opcion:
    print("El elemento esta en la lista")
else:
    print("no esta en la lista")

opcion = 5 in lista

print("opcion: ", opcion)

if opcion:
    print("El elemento esta en la lista")
else:
    print("no esta en la lista")
