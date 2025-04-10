"""
Ingresar una frase de texto por teclado e informar

la letra que mas veces aparece sin contar el espacio

"""

lista_letras = []       # letras que aparecen                              []  ["a", "b", "c", "d"]
cantidad_letras = []    # cantidad de veces que aparece cada letra         []  [ 2,   2,   2,   1] 

frase = input("Ingrese una frase: ")
print("debug: frase:", frase)
frase = frase.replace(" ", "")
print("debug: frase sin espacios:", frase)


for letra in frase:
    if letra in lista_letras:    
        indice = lista_letras.index(letra)
        cantidad_letras[indice] += 1
    
    else:
        lista_letras.append(letra)
        cantidad_letras.append(1)

print("debug: lista_letras:", lista_letras)
print("debug: cantidad_letras:", cantidad_letras)

# buscar el maximo
cant_max = max(cantidad_letras)
print("debug: cantidad_max:", cant_max)