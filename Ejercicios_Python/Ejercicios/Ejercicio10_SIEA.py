#10. Sobre la misma lista modifica el elemento booleano y el primer elemento de la sublista y muestra
#el resultado. Modifica ahora simult´aneamente los dos primeros elementos de la lista y muestra el
#resultado

lista = ["cadena", 3, True, [1, 2], 3.14]
print(f"la lista original es: {lista}")

lista[2] = False
print(f"ahora la nueva lista es: {lista}")

lista[3][0] = 6
print(f"ahora la nueva lista es: {lista}")

lista[0:2] = [8, 9]
print(f"ahora la nueva lista es: {lista}")