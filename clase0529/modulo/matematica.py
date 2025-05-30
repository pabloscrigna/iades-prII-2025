
__all__ = ['suma', 'multiplicar']

def suma(a: int, b: int)->int:
    return a + b


def resta(a: int, b:int)->int:
    return a -b


def multiplicar(a: int, b: int)->int:
    return a * b

if __name__ == "__main__":
    print("Bienvenidos al modulo: ", __name__)
    resultado = suma(5,10)
    print("resultado suma matematica: ", resultado)

    resultado = resta(10, 5)
    print("resultado resta matematica: ", resultado)

    resultado = multiplicar(2,4)
    print("resultado multiplicar matematica: ", resultado)
