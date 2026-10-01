#13. Escribe una sentencia if que compare un valor con 10 y muestre el mensaje correspondiente

valor = int(input("Ingresa un valor: "))

if valor == 10:
    print(f"el valor {valor} es igual")
else:
    print(f"el valor {valor} no es igual")


#otra forma seria
"""if valor == 10:
    print(f"el valor {valor} es igual")
elif valor < 10:
    print(f"el valor {valor} es menor")
else:
    print(f"el valor {valor} es mayor")"""