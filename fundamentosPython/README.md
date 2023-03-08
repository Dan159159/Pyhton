# Curso de Python

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

## Statemnts of Max and Min
```
MAX_INVITADOS = 5
MiN_REUNION = 4
```


## Statemnts of List and tuples
```
# List are mutable
mi_lista = [1, 2, "tres", True]

# Tuples are inmutable
mi_tupla = (1, 2, "tres", True)

Example of tuples
producto1 = ("Camisa", 24.99, 10)
producto2 = ("Pantalón", 34.99, 5)
producto3 = ("Zapatos", 49.99, 2)

productos = [producto1, producto2, producto3]

for producto in productos:
    print("Nombre: ", producto[0])
    print("Precio: ", producto[1])
    print("Cantidad disponible: ", producto[2])
```
## Statements of fuction or procedure

```
def imprimirMensaje():
  print(f"Primera funcion")
  
imprimirMensaje()
```

 

