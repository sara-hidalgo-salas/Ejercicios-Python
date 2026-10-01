#25. Dada una cadena reemplaza las ocurrencias de “a” por “A”. Separa una cadena en subcadenas cuyo
#car´acter de separaci´on es “a”. Convierte una cadena a may´usculas.

#Definimos una cadena
cadena = "una ola"
#CON EL METODO REPLACE REEMPLAZAMOS LA a minuscula por la A MAYUSCULA
print(cadena.replace("a","A"))
#CON EL METODO SPLIT SEPARAMOS LA CADENA ES SUBCADENAS POR EL CARACTER QUE PASEMOS 
print(cadena.split("a"))
#CON EL METODO UPPER PONEMOS LA CADENA EN MAYUSCULAS
print(cadena.upper())



#Si queremos imprimir algo que queramos antes seria:
"""cadena = "una ola"

# Replace
print(f"Reemplazando 'a' por 'A': {cadena.replace('a', 'A')}")

# Split
print(f"Separando por 'a': {cadena.split('a')}")

# Upper
print(f"Convertida a mayúsculas: {cadena.upper()}")"""
