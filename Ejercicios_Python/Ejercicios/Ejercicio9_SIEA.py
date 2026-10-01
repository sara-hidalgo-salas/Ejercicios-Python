#9. Crea una lista que contenga una cadena, un entero, un booleano, una lista y un real. Muestra: la lista completa, 
#el primer elemento de la lista y el primero del elemento lista (sublista), el ´ultimo elemento
#(utilizando ´ındice negativo), los elementos 0 a 2, los elementos de la lista de 2 en 2

lista = ["cadena", 3, True, [1, 2], 3.14]
print(f"la lista completa es la siguiente: {lista}")

primer_elemento = lista[0]
print(f"el primer elemento de la lista es: {primer_elemento}")
#print(f"el primer elemento de la lista es: {lista[0]}")//otra forma de hacerlo mas directo

primer_elemento_sublista = lista[3][0]
print(f"el primer elemento de la sublista es: {primer_elemento_sublista}")
#print(f"el primer elemento de la sublista es: {lista[3][0]}")//otra forma de hacerlo mas directo

ultimo_elemento = lista[-1]
print(f"el ultimo elemento utilizando indice negativo es: {ultimo_elemento}")
#print(f"el ultimo elemento utilizando indice negativo es: {lista[-1]}") //otra forma de hacerlo mas directo

elementoInicioFin = lista[0:3]#inicio:fin el fin no se incluye o sea seria fin-1(el inicio y fin son posiciones)
print(f"los elementos de 0 a 2 son: {elementoInicioFin}")

elementoDos_Dos = lista[0:5:2] #se podria poner vacio el inicio y fin pq detecta cual es el inicio y fin automaticamente ejemp elementoDos_Dos = lista[::2], imprime en el 2 o en el salto que pongamos 
print(f"los elementos de dos en dos son los siguientes: {elementoDos_Dos}")