"""
En base al archivo shoe-data.txt armar una lista de diccionarios

[
    {
     "marca": <marca>,
     "color": <color>,
     "talle": <talle>
    },
    {
    
    }


]
"""

"""
funcion

cadena = '  Adidas	orange	43\n    '
cadena.strip() = 'Adidas    orange  43'
cadena.strip().split('\t') = [ 'Adidas', 'orange', '43']

{
  "marca": "Adidas",
  "color": "orange",
  "talle": "43" 
}
"""

def str_to_dict(cadena: str) -> dict:
    campos = cadena.strip().split('\t')

    return {
        "marca": campos[0],
        "color" : campos[1],
        "talle": campos[2]
    }


zapatillas = [
    str_to_dict(linea)
    for linea in open('shoe-data.txt') 
]

print(zapatillas)