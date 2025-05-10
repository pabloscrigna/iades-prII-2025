

def dividir(a, b):

    if b != 0:
        return a / b

    print("No se puede dividir por cero")


def dividir_new(a, b):

    # if b == 0:
    if not b:
        return None

    return a / b


numero1 = int(input("ingrese num1: "))
numero2 = int(input("ingrese num2: "))

if not numero2:
    print("No se puede dividir por 0")
else:
    resultado = dividir_new(numero1, numero2)

if resultado == None:
    print("Error: No se puede dividir por 0")
else:    
    print("El resultado de la division es: ", resultado)