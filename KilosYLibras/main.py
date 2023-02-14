print("------------------------------------------------------------")
peso=float(input("¿Cuanto pesas? "))
unidad=input("En (kg) ó (lb) : ")
unidad=unidad.lower()
if unidad is str:
    if unidad=="kg":
        conversion=peso*2.205;
        print(f"Pesas {conversion} en lb")
    else:
        conversion=peso/2.205
        print(f"Pesas {conversion} en kg")
else:
    print(f"Dame libras o kg, no {unidad}")
print("------------------------------------------------------------")