"""
Dada una frase, escribir si hay dos caracteres consecutivos iguales

Ejemplo:
frase = "perros" ---> imprime "rr"

i    i+1
p == e      -----> dos letras iguales

i+1  i+1 +1
e == r 

i+1+1 +1       i+1+1 +1 +1  
r    ==        r

frase = "perro" ---> imprime "rr"
frase = "agua" ---> imprime "##"    
"""



frase = "ABCDF"


iguales = "##"

letra_anterior = ""

for letra in frase:
    letra_actual = letra
    if letra_anterior == letra_actual:
        iguales = letra_actual + letra_actual
        break
    else:
        letra_anterior = letra_actual

print(iguales)


letras = "ABCDF"

for x in range(len(letras)-1):
    if letras[x] == letras[x+1]:
        print(f"iguales: {letras[x]} --- {letras[x]}")


