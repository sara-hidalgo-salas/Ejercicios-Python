#27. Crea una funci´on que admita como par´ametro las cadenas “+” o “*” y retorne un puntero a la funci´on
#de suma o producto respectivamente. Invoca dichas funciones a trav´es del puntero obtenido.

def cadenas(parametro):
    def suma():
        print("Esta es la funcion de suma")
    
    def producto():
        print("Esta es la funcion de producto")

    lang_funciones = {"+": suma, "*": producto}
    return lang_funciones[parametro]

funcion_suma = cadenas("+")
funcion_suma()

funcion_producto = cadenas("*")
funcion_producto()