import sys

# los argumentos estan en sys.argv
# sys.argv : una lista con los argumentos. 
print(sys.argv)

argumentos = sys.argv

# print("Nombre del programa: ", sys.argv[0] )
print("Nombre del programa: ", argumentos[0] )


# print("cantidad de argumentos: ", len(sys.argv)-1)
print("cantidad de argumentos: ", len(argumentos)-1)


for i in range(1, len(argumentos)):                    # [ejemplo.py, a, e]      range(1, 3)
    print(f"argumento {i}: {argumentos[i]}")           # [ejemplo.py, a, e, i]   range(1, 4) 
                                                       # [ejemplo.py, a e i, o]  range(1,5)    
    

