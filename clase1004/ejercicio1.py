"""
escribir un programa que pida ingresar una frase e imprima el caracter del medio. Si no tiene
caracter central imprimir caracter vacio


Ejemplo:

frase = "ABC" ---> imprime "B"    3
frase = "ABCD" ---> imprime "##"    4
frase = "ABCDE" ---> imprime "C"    5
frase = "ABCDEF" ---> imprime "##"    6
frase = "perros" ---> imprime "##"    6
"""

frase = input("Ingrese una frase: ")  # ---> perro --> r       

largo = len(frase)  # ---> 6

central = "##"

if largo % 2 != 0:  # Aca entra si tengo un caracter central -- o el largo es impar
    indice = largo // 2  
    central = frase[indice]  

print(central)