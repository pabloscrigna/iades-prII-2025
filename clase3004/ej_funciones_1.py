"""
Hacer una funcion que se le pase un numero entre 0 y 100
 si el numero es par  ---> color = rojo
 si el numero es impar  ---> color = verde


colores(numero, color)

numero: 2  
print("color ", color) ------> "rojo"

numero: 3
print("color ", color) ------> "verde"

"""

def colores(numero, color):
    
    color = "rojo"
    if numero % 2:
        color = "verde"
    print(f"adentro de la funcion: numero: {numero}  -- color: {color}")
    return


color = "sin color"
numero = 5


print(f"antes: numero: {numero}  -- color: {color}")
colores(numero, color)
print(f"despues: numero: {numero}  -- color: {color}")



print("*****************")

persona = {
    "nombre"
    "edad"
}

"""
hacer una funcion para actualizar el nombre de la persona


actualizar_nombre(persona, nombre_nuevo)

"""

def actualizar_nombre(persona, nombre_nuevo):
    persona["nombre"] = nombre_nuevo
    print("adentro de la funcion ** persona: ", persona)
    return


persona = {
    "nombre": "Juan",
    "edad": 56
}

print("antes** persona : ", persona)
actualizar_nombre(persona, "jose")
print("despues ** persona: ", persona)


