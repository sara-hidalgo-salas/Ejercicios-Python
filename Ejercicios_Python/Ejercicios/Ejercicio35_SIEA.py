#35. Crea un m´odulo con el generador definido en el ejercicio 33 de tal manero que pueda invocarse tanto
#desde otro programa como directamente. En caso de invocarlo directamente deber´a mostrar el mensaje
#“Generador de m´ultiplos” y mostrar por pantalla en una l´ınea los m´ultiplos de 5 entre 0 y 30.

import Ejercicio33_35_SIEA

#Con el import llamamos al programa que queramos en este caso el ejercicio 33_35, lo que hace es meterse y leer e imprimir lo que haya en ese programa 
"""Ejercicio33_35_SIEA.generador_multiplos(5, 0, 31)"""#Aqui nos metemos en el .py y lee todo el programa como no hay un print dentro de ese programa lo hacemos aqui abajo ahora para que muestre por pantalla

#Si no tenemos ningun print que muestre la salida en el programa que hemos hecho el import lo tenemos que hacer aqui
print(list(Ejercicio33_35_SIEA.generador_multiplos(5,0,31)))
