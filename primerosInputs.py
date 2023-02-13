"""
print("------------------------------------------------------------")

#print("Hola mundo")
#How create input#
print("------------------------------------------------------------")

    #nombre = input("Cual es tu nombre ")
    #print(f"Tu nombre es {nombre}")
    #print("Tu nombre es " +nombre)

    #edad=input("Cual es tu edad ")
    #print(f"Tu edad es {edad}")
print("------------------------------------------------------------")
#How Create a function#

#def FirstFuction(entrada):return entrada*2
#x="Hola"
#x=7.0
#x=int(x)
#x=FirstFuction(x)
#print(x)
#print(type(x))
print("------------------------------------------------------------")


Preguntar al usuario por su salario. Multiplicar el salario que introduce el usuario por 10, explicándole que podría ganar tanta cantidad si fuera experto en Python 🤣

Preguntar al usuario por 2 números. Sumarlos y mostrar el resultado.

La acción de SANTANDER va cambiando de 3.1453, 2.987 y 3.5. Una aplicación de mainframe con la que compartes datos solo quiere saber el número entero, por ejemplo, 3, 2, 3.

Crear un programa para calcular lo que cada uno tiene que pagar para la cena de una sociedad. Preguntar cuántas personas hay y el precio total de la compra. Por tanto, cada uno tiene que pagar X.

Crear un programa para calcular tu peso en kilos o en libras.

print("------------------------------------------------------------")
salario=int(input("Cual es su salario "))
print(f"Su salario seria {salario*10} si fuera exeperto en python")
print("------------------------------------------------------------")

a=float(input("Dime un numero "))
b=float(input("Dime el segundo numero "))
print(f"La suma es : {a+b}")
print("------------------------------------------------------------")




accion=float(input("A cuanto esta la accion "))
rounded_value = round(accion)
# Printear a lo redondeado
print(f"La accion esta a{rounded_value}")
print("------------------------------------------------------------")

personas=int(input("Cuantas peronas hay en la cena "))
precio=float(input("Cuanto ha salido la cena "))
print(f"Lo que debe pagar cada uno es {precio/personas}")
print("------------------------------------------------------------")
"""
""""
print("------------------------------------------------------------")
peso=float(input("¿Cuanto pesas? "))
unidad=input("En (kg) ó (lb) : ")
if unidad=="kg":
    conversion=peso*2.205;
    print(f"Pesas {conversion} en lb")
else:
    conversion=peso/2.205
    print(f"Pesas {conversion} en kg")
print("------------------------------------------------------------")
#Estructura de if#
if <boolean>
    ....
else:
    ....
"""""
"""""


print("------------------------------------------------------------")
t=float(input("¿A cuentos grados estan esta el agua? "))
tipo=input("En <C> ó <F> : ")
if tipo == "C":
    resultado=float((t * 9 / 5) + 32)
    print(f"La temperatura en Farenheir es : {resultado} cª")
else:
    resultado=float((t  -32)*5/9)
    print(f"La temperatura en Farenheir es : {resultado} fª")

    Celsius = 30  # @param {type:"integer"}
print("------------------------------------------------------------")
"""
"""""
Actividades
Estás trabajando en el área de pruebas para una empresa de finanzas. Crear un programa para confirmar que la variable (inflacion = 3.765) es un tipo float e inmutable. Usar == para comprobar los cambios realizados. Documentar tu código con comentarios. 
PISTA: usar id(), type() y/o instance().

Con las siguientes variables, imprimir la suma de todos que son del tipo int (número entero). La respuesta en este caso es 15.
a = 5
b = 4.32
c = 10
PISTA: usar if, id(), type() y/o instance().

"""
infla=float(input("¿A cuanto esta la inflacion?"))
print(f"La id de la inflacion es : {id(infla)}")
if type(infla) is float:
    print("La inflacion esta en formato float")
else:
    print("La inlacion NO esta en formato float")
#Dato inmutable es el cual solo un id y por lo tanto un valor para la memoria unico, esto agiliza la memoria, casi todas la varbles son variables inmutables, las listas suelen ser mutables por ejemplo.






