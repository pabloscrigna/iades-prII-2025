"""
Controladores iterativos ---> while for
"""


# cuando usas 

# while ---> no se cuantas veces tengo iterar 


# no me gusta nada!!!!!
# while True:
#     pass
# 
#     if True:
#         break

""""
loop infinito
aca si while True

server = init()

while True:

    accept = server()
    accept.return(lahora())
   
"""

# tecla = 1
# 
# while tecla != "s":
#     print("menu")
#     tecla = input()
# 
# 
# while True:
#     print("menu")
#     tecla = input()
# 
#     if tecla == "s":
#         break


numero = 10

while numero < 50:

    num = int(input("numero:"))
    numero += num


# for --> ya se cuantas veces tengo que it 


# for valor in lista_de_valores:

# for : para
# valor: es una variable creada del objeto que se esta iterando
# in En
# lista_de_valores: es la lista/tupla/str que se esta iterando


# range() ---> retorna un iterador
# range(10) --> iterador del 0 al 9
# range(10,100)

for i in range(10):
    print("Hola :", i)

for i in range(10, 100):
    print("Hola n:", i)

for i in range(10, 100, 4):
    print("Hola n:", i)


iterador = range(10)

print(f"type iterador: ", type(iterador))

for i in iterador:
    print(i)


print("Sigue mi programa")


for i in iterador:
    print("new iter: ", i)


frase = "Hola"

for letra in frase:
    print(letra)


lista = [0, 3, 5, 7]
for valor in lista:
    print(lista)

# se puede iterar con un for todo lo que tenga implementado el metodo: __iter__
