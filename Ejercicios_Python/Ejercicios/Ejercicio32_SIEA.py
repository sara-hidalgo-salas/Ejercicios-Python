#32. Utiliza “comprensi´on de listas” para obtener los numeros mayores que 2 de una lista

lista1 = [1, 2, 3, 4, -2]
#esto quiere decir para cada n que hay en lista 1 se haga n>2
lista2 = [n for n in lista1 if n > 2]
print(lista2)