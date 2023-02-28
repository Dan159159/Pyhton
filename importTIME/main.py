
# Funcion que duelve cuanto tarda el programa en sumar todos los numeros naturales de n
import time

# Funcion que suma los valores anteriores a r
def suma_naturales(n):
    inicio = time.time()  # tomamos el tiempo de inicio
    suma = 0
    for i in range(1, n+1):
        suma += i
    fin = time.time()  # tomamos el tiempo de fin
    tiempo = fin - inicio  # calculamos el tiempo total de ejecución
    return (suma, tiempo)
print(f"{suma_naturales(5)}")