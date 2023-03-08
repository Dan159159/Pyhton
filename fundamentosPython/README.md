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
## Statements of class

```
class User:
    nombre = ""
    edad=0
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Esta funcion es para poder imprimir correctamente la clase
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}")
    def setEdad(self, edad):
        self.edad= edad
    def getEdad(self):
        return print(f"{self.edad}")
    def setNombre(self, nombre):
        self.nombre= nombre
    def getNombre(self):
        return print(f"{self.nombre}")


user_1 = User("Carmelo", 2)
user_1.setEdad(24)
user_1.setNombre("Xabi")
user_1.getNombre()
user_1.getEdad()
```
Other option for thec class:
```
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser un número negativo.")
```

# Statements of the inheritance

```
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre.capitalize()

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser un número negativo.")
# This is the inheritance, animal-->dog

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, nueva_raza):
        self._raza = nueva_raza.capitalize()

    # Override del método setter de la edad
    @Animal.edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 20:
            raise ValueError("Los perros no pueden vivir tanto tiempo.")
        super(Perro, Perro).edad.__set__(self, nueva_edad)  # llamado al setter de la clase padre


# Creamos una instancia de la clase Perro y modificamos sus atributos
mi_perro = Perro("Fido", 3, "Labrador")
print(mi_perro.nombre)  # Fido
mi_perro.nombre = "max"
print(mi_perro.nombre)  # Max
mi_perro.edad = 5
print(mi_perro.edad)  # 5
mi_perro.edad = 30  # Lanza una excepción ValueError
```
 

