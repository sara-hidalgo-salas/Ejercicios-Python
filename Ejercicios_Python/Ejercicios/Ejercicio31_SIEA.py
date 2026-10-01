#31. Utiliza “comprensi´on de listas” para sumar los elementos en la misma posici´on de dos listas

l1 = [1, 2, 3]
l2 = [4, 5, 6]

lista_suma = [x + y for x in l1 for y in l2 if l1.index(x) == l2.index(y)]
print(list(lista_suma))



"""OTRA FORMA DE HACERLO CON LA FUNCION ZIP
l1 = [1, 2, 3]
l2 = [4, 5, 6]

#Utilizamos zip para recorrer dos listas
l3 = [x + y for x, y in zip (l1, l2)]
print(l3)"""