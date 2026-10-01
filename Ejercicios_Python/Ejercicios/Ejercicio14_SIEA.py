#14. Dadas dos variables (una par y la otra impar), asigna a otras dos variables las cadenas “par” o “impar”
#seg´un el caso utilizando la asignacion condicional

n1 = 2
n2 = 1

if n1 % 2 == 0 :
    print(f"el numero {n1} es par")
else:
    print(f"el numero {n2} es impar")

if n2 % 2 != 0:
    print(f"el numero {n2} es impar")
else:
    print(f"el numero {n2} es par")


#otra forma mas directo para hacer menos lineas seria con el A if C else B
"""par = "par" if (n1 % 2 == 0) else "impar"
impar = "impar" if (n2 % 2 != 0) else "par"
print(f"{n1} es {par} y {n2} es {impar}")"""