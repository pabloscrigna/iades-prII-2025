"""
Clase Gerente:

Atributos: equipo (lista de empleados), presupuesto (float)
Métodos: contratar_empleado(empleado), despedir_empleado(id_empleado), asignar_proyecto(proyecto, empleado)
Sobrescribir calcular_salario() con bono por tamaño del equipo
"""

from empleado import Empleado

class Gerente(Empleado):

    def __init__(
            self,
            nombre: str,
            apellido: str,
            id_empleado: str,
            salario_base: float,
            presupuesto: float,
            equipo: list[Empleado],
            antiguedad: int = 0,
    ):
        super().__init__(
            nombre,
            apellido,
            id_empleado,
            salario_base,
            antiguedad
        )
        self.presupuesto = presupuesto
        self.equipo = equipo
    
    def contratar_empleado(self, empleado):
        self.equipo.append(empleado)
        return

    

