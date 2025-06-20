"""
Parte 2: Clases Derivadas
Clase Desarrollador:

Atributos: lenguajes (lista), nivel ("Junior", "Semi-Senior", "Senior")
Métodos: programar(proyecto), aprender_lenguaje(lenguaje)
Sobrescribir calcular_salario() con bonos por nivel y cantidad de lenguajes
"""

from empleado import Empleado


class Desarrollador(Empleado):
    BONO_NIVEL = {
        "Junior": 100,
        "Semi-Senior": 1000,
        "Senior": 10000
    }

    def __init__(
            self,
            nombre: str,
            apellido: str,
            id_empleado: str,
            salario_base: float,
            lenguajes: list[str],
            antiguedad: int = 0,
            nivel: str = "Junior"
    ):

        self.lenguajes = lenguajes
        self.nivel = nivel
        super().__init__(
            nombre,
            apellido,
            id_empleado,
            salario_base,
            antiguedad
        )

    def programar(self, proyecto: str) -> str:
        pass

    def aprender_lenguaje(self, lenguaje: str):
        self.lenguajes.append(lenguaje)
        return

    def calcular_salario(self):
        salario = super().calcular_salario()
        bono_nivel = Desarrollador.BONO_NIVEL.get(self.nivel)
        plus_lenguajes = 100 * len(self.lenguajes)
        salario += bono_nivel + plus_lenguajes

        return salario        

if __name__ == "__main__":
    desa = Desarrollador("Juan", "Pecora", "505780", 1000, ["C"], 5, "Senior")
    print(desa.obtener_info_completa())

    desa.lenguajes.append("python")

    print("lenguajes: ", desa.lenguajes)
