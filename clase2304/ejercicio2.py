# dada una frase de una determnada longitud calcular el porcentaje de positividad de un texto"

# las palabras estan en un diccionario 
# 
# palabras_puntos = {
#         "si" : 10,
#         "no" : -10,
#         "alegria" : 8,
#         "tristeza" : -5
# }
# si la palabtra no esta en el diccionario, su puntaje es 0

# salida: el porcentaje de positividad del texto es XX


# frase = "si no hola alegria"
# 
# suma = 10 + (-10) + 0 + 8
# suma = 8  
# promedio = 8 / 4 = 2

# como acceder a un diccionario 
# al diccionario se accede con la clave
# nombre_del_diccionario[nombre_de_la_clave]  ---> warning: si la clave no esta da error
# metodo get nombre_del_diccionario.get(clave)   ---> Si la clave no esta retorna: None
# metodo gel nombre_del_diccionario.get(clave, "no esta")   ---> Si la clave no esta, retorna "no esta"


diccionarios_palabras = {
    "si" : 10,
    "hola" : 8,
    "no": -5
}

frase = input("Ingrese una frase: ")


# proceso la frase
puntaje_total = 0
puntaje_positivo = 0
puntaje_absoluto = 0


print("frase: ", frase)
palabras = frase.split()

print("palabras: ", palabras)
for palabra in palabras:
    print("palabra (clave): ", palabra)
    valor = diccionarios_palabras.get(palabra)
    print("valor: ", valor)


for palabra in palabras:
    puntaje_total += diccionarios_palabras.get(palabra, 0)

promedio = puntaje_total / len(palabras)

# imprimo resultados
print("promedio de positividad es: ", promedio)

