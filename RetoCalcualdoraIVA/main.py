#RETO
preSinIva=float(input("Dime el precio SIN IVA: "))
porcentaje=int(input("Dime el porcentaje de IVA que se quiere aplicar : "))
mas=(preSinIva*porcentaje)/100
resultado=preSinIva+mas
print("------------------------------------------------------------")
if type(porcentaje) is int:
    match porcentaje:

        case 21:
            print(f"Precio Sin IVA : {preSinIva}")
            print(f"IVA: {porcentaje} %")
            print(f"Precio con IVA: {resultado}")
        case 18:
            print(f"Precio Sin IVA : {preSinIva}")
            print(f"IVA: {porcentaje}")
            print(f"Precio con IVA: {resultado}")
        case 15:
            print(f"Precio Sin IVA : {preSinIva}")
            print(f"IVA: {porcentaje}")
            print(f"Precio con IVA: {resultado}")
        case 50:
            print(f"Precio Sin IVA : {preSinIva}")
            print(f"IVA: {porcentaje}")
            print(f"Precio con IVA: {resultado} €")
else:
    "Dame una varible entera de porcentaje de IVA"
print("------------------------------------------------------------")

"""""
                        Codigo para combrobar 
                        
|   Prueba |    Input   |   Output esperado |   Output actual   |  PASS/FAIL   |
|   1   |   IVA 21 Precio 45 |    54.45     |       54.45       |   PASS  |
|   2   |   IVA 18 Precio 45 |    53.1     |       53.1       |   PASS  |
|   3   |   IVA 50 Precio 45 |    67.5     |       67.5       |   PASS  |


"""
