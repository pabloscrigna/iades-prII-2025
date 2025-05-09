def agregar_item(lista: list[int], item: int) -> None:
    """
    Agrega un elemento entero a una lista de numeros enteros.

    :param lista: La lista a la que se le agregará el elemento.
    :param item: El elemento a agregar.
    """

    lista.append(item)
    return






objeto = 5

lista = [8, 6, 8]

valor = int(input("Ingrese un valor: "))

agregar_item(lista, objeto)
agregar_item(lista, valor)

print("lista: ", lista)