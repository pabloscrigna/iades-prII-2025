
# pasando parametros por posicion
# funcion suma

def suma(numero1, numero2):
    return numero1 + numero2


# el 5 se asigna a numero1 y el 6 a numero2
print("la suma de 5 + 6 es: ", suma(5, 6))


# pasando parametros por nombre

def resta(numero1, numero2):
    resultado = numero2 -numero1
    return resultado


print("1 - la resta de 10 - 8 es ", resta(8,10))

print("2 - la resta de 10 - 8 es ", resta(numero1=8,numero2=10))

print("3 - la resta de 10 - 8 es ", resta(numero2=10,numero1=8))


# pasando parametros sin argumentos

def suma(numero1=0, numero2=0):
    resultado = numero1 + numero2
    return resultado

print("s/n-1 la suma de 10 + 20 es ", suma(10,20))
print("s/n-2 la suma de x + x es ", suma())
print("s/n-1 la suma de 10 + 20 es ", suma(10))


