# Curso de Python
## Reto Calculadora IVA

### Codigo para combrobar 
                        
| Prueba | Input | Output esperado | Output actual | PASS/FAIL |
|-------|-------|-----------------|--------------|----------|
| 1     | IVA 21 Precio 45 | 54.45 | 54.45 | PASS |
| 2     | IVA 18 Precio 45 | 53.1 | 53.1 | PASS |
| 3     | IVA 50 Precio 45 | 67.5 | 67.5 | PASS |

## Varibles

```
 numero_Entero = int(10)
 numero_Decimal = float(45151.15114)
 string = "string"
 lista=[1,2,3]
 
```
## Statements if...
```
if <num1 <= num2> :
    print(f"Resultado : {num1} + {num2} = {resultado}")
elif <num3 >= num2 and num4 <= num2> :
    print(f"Resultado de {num3} + {num4}  = {resultado}")
else:
    print("Vaio")
    

```
# Statements switch on py

```
preSinIva=float(input("Dime el precio SIN IVA: "))
porcentaje=int(input("Dime el porcentaje de IVA que se quiere aplicar : "))
mas=(preSinIva*porcentaje)/100
resultado=preSinIva+mas
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
```

## Statemnts for
```

for i in range(1, 6):
    print(i)
```

## Statemnts while
```
i = 1
while i <= 5:
    print(i)
    i +=1
    # += equals i=i+1
```


 

