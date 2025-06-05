

""
from time import sleep

def contar_cinco():
    print("Comienzo a procesar")
    print("Vuelvo")
    yield 100
    print("Sigo procesando")
    print("Vuelvo")
    yield 200
    yield 300
    yield 400
    yield 500


gen_5 = contar_cinco()

print(next(gen_5))
sleep(3)
print(next(gen_5))

print("proceso")
print(next(gen_5))

print(next(gen_5))

# yield 5
print(next(gen_5))

try: 
    print(next(gen_5))
except StopIteration:
    print("No hay mas valores")


# for x in gen_5:
#     print(x)

