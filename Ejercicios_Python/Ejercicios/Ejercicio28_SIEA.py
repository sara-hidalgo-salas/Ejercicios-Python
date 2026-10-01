#28. Utiliza map para sumar los elementos en la misma posici´on de dos listas

def suma(n, m):
    return n + m
l = [1, 2, 3]
l2 = [3, 4, 5]
l3 = map(suma, l, l2)
print(list(l3))


"""OTRA FORMA DE HACERLO
lista1 = [1,2,3]
lista2 = [3,4,5]

#lambda es para hacer funciones simples en una linea
lista_suma = map(lambda x, y: x + y, lista1, lista2)
print(list(lista_suma))"""