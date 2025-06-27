

usuarios = [
    linea.split(":")[0]                                # expresion --- SELECT
    for linea in open("linux-etc-passwd.txt")          # iteracion --- FROM 
    if ":" in linea                                    # condicion --- WHERE 
]  
print(usuarios)