"""
Ejercicio: Sistema de Empleados de una Empresa
Parte 1: Clase Base
Crea una clase Empleado con:
Atributos:

nombre (string)
apellido (string)
id_empleado (string)
salario_base (float)
antiguedad (int, años trabajados)

Métodos:

__init__(nombre, apellido, id_empleado, salario_base, antiguedad=0)
calcular_salario() - salario base + bono por antigüedad (2% por año)
obtener_info_completa() - información detallada del empleado
trabajar() - método genérico
__str__() y __repr__()
"""


class Empleado:

    def __init__(
            self,
            nombre: str,
            apellido: str,
            id_empleado: str,
            salario_base: float,
            antiguedad: int = 0
    ):

        self.nombre = nombre
        self.apellido = apellido
        self.id_empleado = id_empleado
        self.salario_base = salario_base
        self.antiguedad = antiguedad

    def calcular_salario(self):
        bono = (self.salario_base * 0.02) * self.antiguedad
        salario = self.salario_base + bono
        return salario

    def obtener_info_completa(self):
        mensaje = f"Nombre: {self.nombre}, {self.apellido}"
        mensaje = f"{mensaje} id: {self.id_empleado}"
        mensaje = f"{mensaje} antiguedad: {self.antiguedad}"

        return mensaje

    def trabajar():
        return "Aca estamos, trabajando....."


if __name__ == "__main__":
    print(f"Modulo: {__name__}")
    empleado = Empleado("Juan", "Rueda", "505780", 1000000)
    print(empleado.obtener_info_completa())
