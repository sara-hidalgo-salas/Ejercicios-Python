#39. Obten el n´umero de l´ıneas que tiene un fichero y muestra la segunda l´ınea

f = open("archivo.txt")#con open abrimos el archivo 
leer = f.readlines()# readlines lee todas las lineas del archivo txt
print(f"tenemos {len(leer)} lineas")# con len imprimimos el numero de lineas que tiene el archvivo txt 
print(leer[1])# se imprime la posicion de la linea si tenemos 3 lineas como aqui, la posicion 1 es la linea 2
f.close()