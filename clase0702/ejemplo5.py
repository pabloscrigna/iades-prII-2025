# operador walrus (:=)
# este operador permite asignar una variable dentro de una expresion,
# en lugar de hacerlo en una linea separada


linea = input("Ingrese una palabra: ")

print("sin operador")
while linea != "salir":
    print("palabra: ", linea )
    linea = input("Ingrese una palabra: ")

print("con operador")
# imprimir la palabra ingresada, salir para terminar
while((linea:= input("ingrese una palabra: ")) != "salir"):
    print("palabra: ", linea)
