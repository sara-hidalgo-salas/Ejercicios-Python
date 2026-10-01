#33. Utiliza un generador para mostrar por pantalla los m´ultiplos de 5 entre 0 y 50. Utiliza el mismo
#generador para mostrar los m´ultiplos de 3 entre 4 y 31


#Ahora lo haremos con funciones para el ejercicio 35, Un generador se usa cuando una sola función debe producir MUCHOS valores uno tras otro.
def generador_multiplos(multiplo, inicio_rango, final_rango):
    for n in range(inicio_rango,final_rango):
        if n % multiplo == 0 :
            yield n
            
print(list(generador_multiplos(5, 0, 51)))
print(list(generador_multiplos(3, 4, 31)))



#esto quiere decir para cada n en el rango de 0 a 50 (pq range va desde el inicio hasta el final menos 1)
#que n va a ser cada elemento del range se haga n%5 == 0 para saber si es multiplo
"""multiplos_5 = (n for n in range (51) if n % 5 == 0)
print(list(multiplos_5))

multiplos_3 = (n for n in range (4,32) if n % 3 == 0)
print(list(multiplos_3))"""
#Utilizamos list para mostrar pon pantalla el resultado si no se utiliza nos daria algo parecido a: <generator object <genexpr> at 0x0000013C9E459E50>


#Ahora lo con dos funciones diferentes
""""
def multiplos_5(x, y):
    for n in range(x,y):
        if n % 5 == 0 :
            yield n

print(list(multiplos_5(0, 51)))


def multiplos_3(x, y):
    for n in range(x,y):
        if n % 3 == 0 :
            yield n #yield lo usamos en generadores, genera valores, que luego puedes usar como quieras

print(list(multiplos_3(4, 31)))"""