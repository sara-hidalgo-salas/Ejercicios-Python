#38. Muestra en una sola linea los par´ametros pasados como argumento (no incluir el nombre del programa)

import sys

#esto dice: si el tamaño de los argumentos es mayor que uno, uno va a ser el nombre del programa (pq de momento hablamos de tamaño) 
#imprime desde la posicion 1 hasta el final (ya que poscion 0 es el nombre del programa y la posicion 1 hacia delante los argumentos)
if len(sys.argv) > 1:
    print("Argumentos:", sys.argv[1:])
else:
    print("Escribe mas argumentos")