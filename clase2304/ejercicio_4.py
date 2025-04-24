# merge de diccionarios

diccionario1 = {
    "nombre": "pablo",
    "apellido": "perez"
}

diccionario2 = {
    "edad": 34,
    "peso": 56
}

diccionario3 = {**diccionario1}

print("diccionario3:", diccionario3)

diccionario3 = {**diccionario1, **diccionario2}

print("diccionario3:", diccionario3)


# todos mis requests http van a tener estos valores en el header
headers = {
    "content-type": "application/json"
}

api_key = {"apikey": "ASSFDGDGFDGDFHFH"}
headers_post = {**headers, **api_key}

print(headers_post)