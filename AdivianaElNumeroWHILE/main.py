# Reto Adivina el numero con WHILE
import random
rnd = random.randint(1, 100)
print("Adivina el numero entre el 1 y 100")
res = int(input("Introduce un numero entero : "))
print("------------------------------------------------------------")
while res != rnd:
    if res > rnd:
        print(f"El número misterioso es menor que {res}.")
        res = int(input("Introduce un numero entero : "))
    else:
        print(f"El número misterioso es mayor que {res}.")
        res = int(input("Introduce un numero entero : "))
else:
    print("¡Felicidades, has acertado!")