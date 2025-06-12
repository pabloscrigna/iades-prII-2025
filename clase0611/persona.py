from datetime import datetime

class Persona:

    def __init__(self,nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.nombre_apellido = f"{self.nombre}, {self.apellido}"
        self.fecha = datetime.now()
    
    def datos(self):
        print(f"nombre completo: {self.nombre}, {self.apellido}")
        print(f"edad: {self.edad}")
        mensaje = f"{self.nombre_apellido} [{self.edad}]"
        return mensaje   

    # metodo de la clase Persona
    def imprimir(self):
        # retorne un string nombre,apellido,edad,dni,fecha    
        return f"{self.nombre},{self.apellido},{self.edad},{self.dni},{self.fecha}\n"

    def __str__(self):
        return f"nombre: {self.nombre}"