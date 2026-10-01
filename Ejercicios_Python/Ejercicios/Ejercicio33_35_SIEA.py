#Ejercicio 33_35

def generador_multiplos(multiplo, inicio_rango, final_rango):
    for n in range(inicio_rango,final_rango):
        if n % multiplo == 0 :
            yield n
            
            
#Usamos if __name__ == "__main__" para que el código dentro de este bloque solo se ejecute si el archivo se ejecuta directamente, evitando que se ejecute al importar el módulo desde otro archivo.
if __name__ == "__main__":
    # Código dentro de este bloque solo se ejecuta
    # cuando ejecutamos el archivo directamente,
    # no cuando lo importamos desde otro programa.
    print ("generador de multiplos")
    print(list(generador_multiplos(5, 0, 31)))