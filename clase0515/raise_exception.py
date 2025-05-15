
def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    
    if n == 0:
        return 1
    
    return n * factorial(n - 1)


try:
    n = int(input("Ingrese un numero para calculcular su factorial: "))
    print(factorial(n))
except ValueError:
    print(f"No se puede calcular el factorial de {n}")
