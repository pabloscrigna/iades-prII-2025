
def calculadora (b, c, a):

    if a == "suma":
        resultado = (b + c)
    elif a == "resta":
        resultado = b - c    
    else:
        resultado = "operacion no valida!!"
    
    return resultado


# sacar num1 y num2 de un archivo y sumar()
# tira un get a esta api y te va a retorna dos valores sumalos

# Obtenemos los datos
a = input("ingresa el tipo de operación: ")
b = int(input("Ingresa el primer numero"))
c = int(input("ingresa el segundo numero"))

resultado = calculadora(a,b,c)