#26. Dada una lista de 3 elementos, inserta un nuevo elemento en la segunda posici´on y obt´en su posici´on.
#Invierte la lista y vuelve a mostrar la posici´on. Ordena la lista.

#Definimos una lista
lista = [1,2,3]
#INSERTAMOS UN NUEVO ELEMENTO EN LA SEGUNDA POSICION
lista.insert(2,5)
print(lista)
#OBTENEMOS LA POSICION DEL ELEMENTO AÑADIDO
print(lista.index(5))
#INVERTIMOS LA LISTA
lista.reverse()
print(lista)
#OBTENEMOS LA POSICION DEL ELEMENTO
print(lista.index(5))
#ORDENAMOS LA LISTA 
lista.sort()
print(lista)