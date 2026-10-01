#29. Utiliza filter para obtener los numeros mayores que 2 de una lista

def mayorDos(n):
    return (n>2)
l = [1,2,3,4,5,-2]
            #funcion,secuencia -> nuestra l (los elementos que tiene dentro l) pasaria a ser la n
l2 = filter(mayorDos,l)# filter ...(buscar q hace)
print(list(l2))