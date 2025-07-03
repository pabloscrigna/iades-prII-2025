### 
# Armar un dict donde la key sea el username y el valor sea el shell 

# diccionario = { "user": "shell", "user": "shell" }

diccionario = {
    linea.split(":")[0] : linea.split(":")[-1].strip()
    for linea in open("linux-etc-passwd.txt")
    if ":" in linea
}

print(diccionario)


