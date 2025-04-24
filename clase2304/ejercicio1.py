"""
Dada una frase imprimir las palabras (sin considerar los espacios)

"""


frase = "Bienvenidos al curso de programacion II"

# separa al string por el caracter de separacion que se le pasa como argumento. Por default si no se especigfica un caracter de separacion
# separa por el espacio. Retorna una lista con los strings separados
# caracter de separacion: a
# 0: Bienvenidos 1: l curso de progr 2: m 3: cion II
frase1 = frase.split()

# lista con las palabr
print(frase1)   

for palabra in frase1:
    print("palabra: ", palabra)


texto = "hol  mi nombre es raul agustin"
resultado = texto.split("a")
print(resultado)