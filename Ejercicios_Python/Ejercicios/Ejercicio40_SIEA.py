#40. Muestra las l´ıneas de un fichero que concuerdan con una ER pasada como par´ametro. Si no se pasa
#ning´un par´ametro se mostrar´a un mensaje de error.

import sys
import re

#aqui decimos: si la longitud de los argumentos es menor a 2 o sea si no se le pasa argumentos o solo el nombre del programa da error, si es 2 o mayor que 2 nos vamos al else
if len(sys.argv) < 2:
    print("Error: no se ha pasado ninguna expresión regular.")
else:
    patron = sys.argv[1]# guardamos el primer argumento que sera lo que estamos buscando en el txt
    archivo = open("archivo.txt")# abrimos el archivo
    for linea in archivo:#recorremos el archivo
        if re.search(patron, linea):#buscamos en todo el archivo donde aparezca el parametro que hayamos pasado en este caso ER
            print(linea, end="")#imprimimos la linea donde aparece y con end evitamos el doble salto de linea