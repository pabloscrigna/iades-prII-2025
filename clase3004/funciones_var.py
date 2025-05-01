figura = "cuadrado"   # global


def area_figura(lado_a, lado_b):

    if figura == "cuadrado":    # global
        area = 2 * lado_a
        print(f"el area de {figura} es: {area}")

    return area


def perimetro(lado_a, lado_b):
    # figura = "triangulo"     # es local la funcion perimetro
    if figura == "cuadrado":  
        print(f"el perimetro de {figura} es: {2 * lado_a}")
    else:
        print(f"la figura es un {figura}")
    return 

def suma(numero1, numero2):
    resultado = num1 + num2
    print("el resultado es: ", resultado)
    return

def resta(num1, num2):
    resultado = num2 -num1
    print("resultado: ", resultado)
    return

def resta_1(num1, num2):
    resultado = num2 - num1
    return resultado 

# area_figura(3,5)
# perimetro(5, 8)


# suma(5, 8)
# suma(8, 5)


# resta(5, 8)
# resta(8, 5)

print("debug resta_1")

resultado1 = resta_1(5, 8)
print("resultado1: ", resultado1)

resultado2 = resta_1(10,6)
print("resultado2: ", resultado2)

resultado3 = resta_1(11,7)
print("resultado3: ", resultado3)

numero1 = 10
numero2 = 20

resultado = suma(10, 10)
print("resultado de suma: ", resultado)