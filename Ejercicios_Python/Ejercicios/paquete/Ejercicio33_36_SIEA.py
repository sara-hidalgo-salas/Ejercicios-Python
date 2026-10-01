#Ejercicio 33_36

def generador_multiplos(multiplo, inicio_rango, final_rango):
    for n in range(inicio_rango,final_rango):
        if n % multiplo == 0 :
            yield n
            