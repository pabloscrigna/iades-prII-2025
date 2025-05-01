"""
Hacer una funcion calculadora 

calc(num_a, num_b, operacion)
num_a : entero 
num_b : entero
operacion : str   "+" "-" "*" "/"

Retorna

el resultado de la operacion entre num_a y num_b

calc(10, 2, "/") ---> retorna 5
calc(10, 2, "*") ---> retorna 20
"""

def calc(num_a, num_b=1, operacion="+"):

    if(operacion == "+"):
        return num_a + num_b

    if(operacion == "-"):
        return num_a - num_b
     
    if(operacion == "*"):
        return num_a * num_b

    if(operacion == "/"):
        # verificar divison por cero
        if num_b: 
            return num_a / num_b
        else:
            return "No se puede dividir por 0"

    return "Operador no valido"


print("probando suma : ", calc(10,10,"+"))
print("probando resta: ", calc(10,10,"-"))
print("probando multiplicacion: ", calc(10,10,"*"))
print("probando division s/0", calc(10,2,"/"))
print("probando division s/0", calc(10,0,"/"))
print("probando division c/0", calc(10,0,"xxxx"))

print("probando operacion suma default: ", calc(10,10))

print("probando operacion suma default: ", calc(10,10))


print("probando operacion suma default: ", calc(num_b=10))

