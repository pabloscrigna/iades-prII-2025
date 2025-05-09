def calculadora(numero1: int, numero2: int, op: bool )-> int | float:
    """
    Funcion calculadora

    numero1: primer operando de tipo entero
    numero2: segundo operando de tipo entero

    op: bool

    True: retorna el resultado de la suma de numero1 y numero2
    False: retorna el resultado de la division de numero2 / numero1
    """


    if op:
        return numero1 + numero2
    else:
        return numero2 / numero1


# numero1 numero2 op : obligatorios 
result =calculadora(5, 10)

print("resultado de a suma: ", result)


result =calculadora(5)

print("resultado de a suma: ", result)