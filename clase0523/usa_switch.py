"""
switch(case)  -----> python 3.10 en adelante

"""

opcion = 7

match opcion:

    case 1:
        print("ingreso la opcion 1")
    case 2:
        print("ingreso la opcion 2")
    case 3:
        print("Ingreso la opcion 3")
    case _ :
        print("No existe la opcion")


tecla = "2"

match tecla:

    case "1":
        print("ingreso la opcion 1")
    case "2":
        print("ingreso la opcion 2")
    case "3":
        print("Ingreso la opcion 3")
    case _ :
        print("No existe la opcion")