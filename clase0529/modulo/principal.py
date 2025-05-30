"""
vamos a importar las funciones del moduko matematica
"""

numero1 = 10
numero2 = 20

# 1 forma

# import matematica
# 
# resultado = matematica.suma(numero1, numero2) 
# print("resultado de la suma principal: ", resultado)
# 
# resultado = matematica.resta(numero1, numero2) 
# print("resultado de la resta principal: ", resultado)


# 2 forma

# from matematica import *
# 
# resultado = suma(numero1, numero2) 
# 
# print("resultado de la suma: ", resultado)
# 
# resultado = resta(numero1, numero2) 
# print("resultado de la resta: ", resultado)

# 3 forma 
from matematica import suma, resta 

if __name__ == "__main__":
    print("Bienvenidos al modulo: ", __name__)

    resultado = suma(numero1, numero2) 
    print("resultado de la suma: ", resultado)

    resultado = resta(numero1, numero2) 
    print("resultado de la resta: ", resultado)

# 4 forma, importando solo suma

# from matematica import suma 
# 
# resultado = suma(numero1, numero2) 
# print("resultado de la suma: ", resultado)


# 5 forma 

# from matematica import suma as sm
# 
# resultado = sm(numero1, numero2)
# print("resultado suma: ", resultado)




