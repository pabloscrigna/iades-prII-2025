"""
Pida al usuario ingresar numeros e ir sumandolos, hasta que ingresa el 0 
"""

contador = 0
entrada = int(input("Ingresar 0 para salir: ")) 
while entrada != 0:
    contador += entrada
    entrada = int(input("Ingresar 0 para salir: "))    

print("suma ", contador)
print("Termino sin op")

# operador walrus --- malo del pajaro loco
# variable := len(frase) > 10  -- asigna y evalua

contador_wl = 0
while (entrada := int(input("Ingrese un numero - 0 para salir: "))) != 0:
    contador_wl += entrada


print("contador 2: ", contador_wl)
