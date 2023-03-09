class Empleado:
    def __init__(self, nombre, salario):
        self._nombre=nombre
        self.__salario=salario
    def __str__(self):
        print(f"La empleade {self._nombre} cobra {self.__salario}")
    def calcular_salario(self):
        self.__salario *= 1.1
        return round(self.__salario)

    def get_salario(self):
        return self.__salario
class Programador (Empleado):
    def __init__(self, nombre, salario, lenguaje_programacion):
        super().__init__(nombre, salario)
        self._lenguaje_programacion = lenguaje_programacion
class Sistema_Nominas:
    def calcular_nominas(self, empleados):
        print(f"Calculando nominas")
        print(f"==================")
        for empleado in empleados:
            print(f"Nomina para : {empleado._nombre} - {empleado._lenguaje_programacion}")
            print(f"€ : {empleado.calcular_salario()}")
            print("")