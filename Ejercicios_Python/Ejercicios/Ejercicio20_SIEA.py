#20. Escribe una funci´on que imprima los par´ametros que se la han pasado (n´umero variable) de dos
#maneras: 1) uno en cada l´ınea y 2) como una tupla

def funcion(*variables):#el* es para poner todas las variables que queramos sin tener que ir definiendolas
    for i in variables:# i van a ser las variables y variables va a ser donde estan guardados cada variable
        print(i)
    print(variables)

#como hacemos el print dentro de la funcion solo es necesario llamar a la funcion y ya
funcion(1,2,3,"hola","adios", [1,2,3])