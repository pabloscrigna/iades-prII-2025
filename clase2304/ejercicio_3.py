
permisos = {

    "lectura" : ["inventario", "leads"],
    "escritura" : ["inventario", "leads"]
}


# armar la lista con los permisos donde
# 0 --> lectura & escritura
# 1 --> lectura
# 2 --> escritura


usuarios_permisos = []

permiso_0 = permisos.copy()

usuarios_permisos.append(permiso_0)

print("permisos paso 1:", usuarios_permisos)

permiso_1 = permisos.copy()

del permiso_1["escritura"]

usuarios_permisos.append(permiso_1)

print("permisos paso 2:", usuarios_permisos)

