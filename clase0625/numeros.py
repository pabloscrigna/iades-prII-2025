
numeros = [5, 6, 7, 8, 9, 10]

resultado = sum(numeros)

print(f"La suma de los números es: {resultado}")

linea = "       67        "

print(f"La línea original es: '{linea}'")
linea = linea.strip()  # Elimina espacios al inicio y al final
print(f"La línea después de strip es: '{linea}'")

numeros = []

with open("nums.txt", "r") as file:
    for linea in file:
        if linea.strip():
            # print(linea.strip())
            numeros.append(int(linea.strip()))
    resultado = sum(numeros)
    print(resultado)