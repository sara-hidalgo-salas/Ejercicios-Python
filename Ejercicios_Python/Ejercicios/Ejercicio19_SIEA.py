#19. Escribe una funci´on que muestre la suma de dos n´umeros (o cadenas). Aplica la funci´on a dos n´umeros y dos cadenas

def sum(num1, num2, cad1, cad2):
    suma = num1+num2
    sum_cad=cad1+cad2
    return suma, sum_cad

print(sum(1,2,"ho","la"))


"""#otra opcion seria imprimirlo directamente dentro del def seria asi:
def sum(num1, num2, cad1, cad2):
    suma = num1+num2
    sum_cad=cad1+cad2
    print(suma, sum_cad)
sum(1,2,"h","o")

#la otra opcion mas directa es hacerlo dentro del print
def sum(num1, num2, cad1, cad2):
    print(f"el resultado de la funcion es: {num1+num2, cad1+cad2}")
sum(1,2,"h","o")


def sum(num1, num2, cad1, cad2):
    return num1+num2, cad1+cad2
suma = sum(1,2,"h","o")
print(f"el resultado de la funcion es: {suma}")"""