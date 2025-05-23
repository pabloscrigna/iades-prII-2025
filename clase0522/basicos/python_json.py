# importamos el modulo json
import json


# creamos una lista en python
lista = ["a", "e", "i"]


# transformar la lista en python a un string json
lista_json = json.dumps(lista)

print(lista_json)


# vamos a transformar lista_json a una lista en python

lista_python = json.loads(lista_json) 


