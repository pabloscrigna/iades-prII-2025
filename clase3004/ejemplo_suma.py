


# defino la funcion suma
def suma(num1, num2):
    resultado = num1 + num2
    print("el resultado es: ", resultado)
    return  resultado


# variables
numero1 = 10
numero2 = 20

resultado = suma(10, 10)
print("resultado de suma: ", resultado)

resultado = suma(numero1, numero2)


valor1 = 30
valor2 = 50

resultado = suma(valor1, valor2)
print("resultado de suma: ", resultado)


# Quiero sumar 3 numeros usando la funcion suma(a,b)

a = 56
b = 45
c = 78

# resultado = a + b + c

resultado = suma(a,b)
resultado = suma(c, resultado)    # a + b

print(f"el resultado de {a} + {b} + {c} es {resultado}")