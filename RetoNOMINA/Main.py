import  Nominas as m
Jon= m.Programador("Jon", 1450,"Python")
Maria = m.Programador("Maria", 1500, "Java")
Leo = m.Programador("Leo", 750, "HTML")
empleados = []

if __name__ == '__main__':
    empleados.append(Jon)
    empleados.append(Maria)
    empleados.append(Leo)
    sistema = m.Sistema_Nominas()
    sistema.calcular_nominas(empleados)