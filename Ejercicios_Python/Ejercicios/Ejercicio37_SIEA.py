#37. Lee n´umeros del teclado hasta que se introduzca un 0. Si no se introduce un n´umero indica el
#error mediante una excepci´on. Al introducir un 0 muestra el mensaje “Fin” capturando la excepci´on SystemExit.

try:
    num = int(input("Introduce un numero\n"))
    while num != 0:
        num = int(input("Introduce otro numero o 0 para finalizar\n"))
    else:
        exit()# Esto lanza SystemExit
except ValueError:
    print("Error, no has introducido un numero.")
except SystemExit:
    print("Fin")



#Otra version, en esta version si se escribe una cadena no se finaliza, te pide otro numero
"""num = int(input("Introduce un numero\n"))
T = True
while T:
    try:
        if (num != 0):
            num = int(input("Introduce otro numero o 0 para finalizar\n"))
        else:
            T = False
            exit()# Esto lanza SystemExit
    except ValueError:
        print("Error, no has introducido un numero, vuelve a intentarlo.\n")
    except SystemExit:
        print("Fin")



#Otra version con break
while True:
    try:
        num = int(input("Introduce un numero o 0 para salir:\n"))
        if num == 0:
            exit()
    except ValueError:
        print("Error, no has introducido un numero.")
    except SystemExit:
        print("Fin")
        break"""