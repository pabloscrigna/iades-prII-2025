lista = []
opcion = ""


while opcion != "3":

    print(
        "ingrese una opcion\
          1- Insertar\
          2- Sacar\
          3- Salir"
    )

    opcion = input("Ingresar una opcion: ")

    if opcion == "1":
        valor = input("ingresar un valor")
        lista.append(valor)
        print("lista: ", lista)
        print(
            """

            """
        )
    elif opcion == "2":
        # if len(lista) > 0:
        if lista:
            print("sacamos el elemento: ", lista.pop())
            print("lista: ", lista)
        else:
            print("la lista esta vacia")
        print(
            """

            """
        )


print("Gracias por venir!!!")
