"""
Ingressar por teclado numeros separados por espacios
Sumar los numeros, pero considerando cada numero solo una unica vez

por ejemplo:

'10 20 10 20'

resultado = 30

"""


# ingresamos el string de numeros

valores = input("Ingresar numeros separados por espacios: ")

suma = sum({
    int(numero)
    for numero in valores.strip().split()
})

print("suma :", suma)