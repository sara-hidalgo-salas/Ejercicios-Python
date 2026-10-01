#12. Crea un diccionario que asocie nombres de personas con nombres de ciudades. Mu´estralo. Muestra la
#ciudad asociada al segundo nombre. Modifica la ciudad asociada al primer nombre.

diccionario = {"Juan": "Madrid", "Luis": "Barcelona"}
print(f"mi diccionario es el siguiente: {diccionario}")

print("la ciudad asociada al segundo nombre es la siguiente: " + diccionario["Luis"])

#Otra forma seria ponerlo con comilla simple
#print(f"la ciudad asociada al segundo nombre es la siguiente: {diccionario['Luis']}")

#Otra forma seria inicializando una variable
#segundo_nombre = diccionario["Luis"]
#print(f"la ciudad asociada al segundo nombre es la siguiente: {segundo_nombre}")