"""
Dada una frase, sacarle los "."
"""

frase = "sds.dsa.dsaf"  # ---> sdsdsadsaf

# frase = sds.dsa.dsa

for i in range(len(frase)):
    if frase[i] == ".":
        print("Encontro un .")
        frase = frase[:i] + frase[i+1:]