"""
programa para sumar dos enteros
"""

num1 = 89
num2 = 1

# 1 forma
# import matematica
# 
# print(matematica.suma(num1, num2))
# print(matematica.resta(num1, num2))

# 2 forma

# from matematica import *
# 
# print(suma(num1, num2))
# print(resta(num1, num2))


# 3 forma

# aca solo se importa la funcion suma
from matematica import suma, resta
#
print(suma(num1, num2))

# 4 forma

# from matematica import suma as sm

# print(sm(num1, num2))