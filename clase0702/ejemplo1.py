lista = list(range(10))
print("lista: ", lista )

# lista **2

lista_2 = [ x**2 
           for x in lista ]

print("lista al 2 : ", lista_2)
 

lista_pares = [ x
              for x in lista 
              if x % 2 == 0]

print("lista_ pares: ", lista_pares)


# dada una lista con palabras, sacar las vocales

lista = [ "python", "casa" ]

lista_sin_vocales = [ "".join(letra)
                     for palabra in lista
                     for letra in palabra
                     if letra not in "aeiou"
]

print("lista sin vocales: ", lista_sin_vocales)


lista = ["python", "casa", "luz"]

sin_vocales = [''.join([letra for letra in palabra if letra not in "aeiou"]) 
               for palabra in lista
            ]
print(sin_vocales)