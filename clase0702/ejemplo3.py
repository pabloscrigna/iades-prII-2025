lista = ['a=1', 'b=2', "c=3"]


# {"a": 1, "b": 2, "c":3}

diccionario = {
    item.split("=")[0] : item.split("=")[1]
    for item in lista
}

print(diccionario)