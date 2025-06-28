s = "python es un lenguaje de programacion" \

# [(python, 6), (es, 2), (un, 2)]


salida = [
    (palabra, len(palabra)) 
    for palabra in s.split()
]

print(salida)
