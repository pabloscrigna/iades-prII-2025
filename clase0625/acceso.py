filename = "mini-access-log.txt"

direcciones = []

with open(filename, "r") as file:
    for line in file:
        direcciones.append(line.split()[0])

print(direcciones)