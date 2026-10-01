#17. Solicita una palabra por teclado hasta que se introduzca la palabra “fin”

palabra = input("introduce una palabra: ")

while palabra != "fin":
    palabra = input("introduce otra palabra o fin para terminar: ")#guardamos la nueva palabra en una variable ya que si hacemos print se queda en un bucle infinito
else :
    print("se introdujo la palabra fin")