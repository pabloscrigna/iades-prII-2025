# Dado el archivo nums.txt, sumar los numeros
# una linea tiene como maximo un numero o ningun numero

resultado = sum([
    int(linea.strip())
    for linea in open("nums.txt")
    if linea.strip()
])

print("resultado: ", resultado)