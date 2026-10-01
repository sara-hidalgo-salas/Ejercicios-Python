#34. Captura el error al intentar aceder a un ´ındice de una lista que no existe. Lo mismo para la clave de
#un diccionario

lista1 = [1, 2, 3]
try:
    print(lista1[3])
except(IndexError):#Aqui ponemos que es indexError pq es el error que nos marca pero podrian ser otros errores
    print("No existe ese indice en la lista")


diccionario = {"Nombre": "Luis"}
try:
    nombre = diccionario["Apellido"]
    print(nombre)
except(KeyError):
    print("\nNo existe esa clave en el diccionario") 