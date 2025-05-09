def calculadora(numero1: int, numero2: int,op: bool = True)-> int | float | None:

    if op:
        return numero1 + numero2

    else:
        return numero2 / numero1



result = calculadora(5,5,True)
print("resultado suma: ", result)

result = calculadora(5,5)
print("resultado suma: ", result)

result = calculadora(5,5, True)
print("resultado suma: ", result)

result = calculadora(5,5,False)
print("resultado division: ", result)