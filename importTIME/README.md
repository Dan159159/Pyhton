# IMPORT TIME
The module time is used usually to know is what time one process is finished or to slep a short moment the program

## Get on what time the program finished the code
```
import time

inicio = time.time()

# código a medir

fin = time.time()

tiempo_total = fin - inicio
print(f"El tiempo de ejecución del programa fue de {tiempo_total} segundos.")
```
# Stand by the code for a exactly minutes
```
import time
tiempo = 5
print("Comenzando tarea...")
time.sleep(tiempo)
print("Tarea completada.")
```
```
import time
DORMIR = 3
def mens():
    print(f"HE DESPERTADO")

time.sleep(DORMIR)
mens()
```
#### Obtener el tiempo actual en segundos desde la época:
```
tiempo_actual = time.time()
print(tiempo_actual) 
```
#### # Convertir una cadena de tiempo en formato de fecha/hora en segundos desde la época:

```
import time

cadena_tiempo = "2022-02-23 10:30:00"
tiempo_sec = time.mktime(time.strptime(cadena_tiempo, "%Y-%m-%d %H:%M:%S"))
print(tiempo_sec)

```

