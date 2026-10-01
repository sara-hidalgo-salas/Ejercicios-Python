#16. Almacenar los valores entre 20 y 1 en una lista y mostrarla (ayuda: se pueden concatenar listas con
#el operador +)

mi_lista = [] 
# Para ir del 20 al 1, usamos -1 para ir restando de uno en uno 
for i in range(19, 0, -1):
    mi_lista.append(i) # Esto agrega el número al final de la lista
print(f"mi lista entre 20 y 1 seria: {mi_lista}") # Muestra cómo crece la lista en cada vuelta


"""#otra forma de hacerlo seria con while
num = 19
while num >= 1:
    mi_lista.append(num)
    num = num - 1
print(f"mi lista entre 20 y 1 seria: {mi_lista}")"""