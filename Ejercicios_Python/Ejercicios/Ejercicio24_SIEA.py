#24. Define un diccionario y utiliza el m´etodo get para obtener el valor asociado a una clave. Si la clave no
#existe devueve la frase “No est´a”. Muestra el dicionario completo, solo las claves y solo los valores.


                #clave      #valor
diccionario = { "Nombre" : "Luis", "Apellido": "Perez", "Num" : 1}

#MOSTRAMOS CON EL METODO GET, EL VALOR ASOCIADO A LA CLAVE NOMBRE 
print(diccionario.get("Nombre"))
print()

#MOSTRAMOS CON EL METODO GET QUE LA CLAVE HOLA NO ESTA EN EL DICCIONARIO
print(diccionario.get("hola", "La clave hola no esta"))
print()

#MOSTRMAOS EL DICCIONARIO COMPLETO
print(f"Mi diccionario completo es: {diccionario}")
print()

#MOSTRAMOS CON EL METODO KEYS SOLO LAS CLAVES
print(f"Mis claves son: {diccionario.keys()}")

#SI NO QUEREMOS QUE APAREZCA EL DICT_KEYS AL IMPRIMIR LO PONEMOS COMO UNA LISTA Y QUEDA:
print(f"Mis claves como lista son: {list(diccionario.keys())}")
print()

#MOSTRAMOS CON EL METODO VALUE TODOS LOS VALORES
print(f"Mis valores son: {diccionario.values()}")

#SI NO QUEREMOS QUE APAREZCA EL DICT_KEYS AL IMPRIMIR LO PONEMOS COMO UNA LISTA Y QUEDA:
print(f"Mis valores como lista son: {list(diccionario.values())}")