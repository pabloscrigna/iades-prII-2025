
from vector import Vector


v1 = Vector([2,4])

v2 = Vector([10,5, 8])

print("v1: ", v1.datos)

print("v1: ", v1)
print("v2: ", v2)

print("largo v1", len(v1))
print("largo v2", len(v2))

print(f"v1[0]: {v1[0]} -- v1[1]: {v1[1]}")

v1[0] = 34
v1[1] = 67

print(f"v1[0]: {v1[0]} -- v1[1]: {v1[1]}")


for valor in v1:
    print(valor)
