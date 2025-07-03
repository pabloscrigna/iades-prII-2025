s = "python es un lengaje de programacion"

# [ ("python", 6), ("es", 2), ("un", 2)]

# { "python": 6 }

#s = [("a", 2), ("b", 3)]   # list(tuple)
#print(dict(s))


diccionario = dict([ (palabra, len(palabra))
    for palabra in s.split()                         # [ "python", "es", "un"]
])

print(diccionario)


diccionario = {
    palabra : len(palabra)
    for palabra in s.split()
}