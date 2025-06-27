# usuarios = set([
#     linea.split(":")[0]                                # expresion --- SELECT
#     for linea in open("linux-etc-passwd.txt")          # iteracion --- FROM 
#     if ":" in linea                                    # condicion --- WHERE 
# ])



usuarios = {
    linea.split(":")[0]                                # expresion --- SELECT
    for linea in open("linux-etc-passwd.txt")          # iteracion --- FROM 
    if ":" in linea                                    # condicion --- WHERE 
}

print(usuarios)
print(type(usuarios))

if 'root' in usuarios:
    print("El usuario root existe en mi sistema")

