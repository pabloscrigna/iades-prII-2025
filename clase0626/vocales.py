# tengo una frase y quiero saber cuantas vocales hay en la frase 


s = "palabras"

cantidad = sum([
    1
    for letra in s
    if letra in "aeiou"
])

print(cantidad)