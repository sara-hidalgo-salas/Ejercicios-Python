#21. Escribe una funci´on que retorne la suma y el producto de dos n´umeros

def op(num1, num2):
    suma=  num1+num2 
    mul = num1*num2
    return suma,mul

#cuando ponemos return en la funcion tenemos que hacer un print despues con la funcion para que se muestre por pantalla
print(f"el resultado seria : {op(4,4)}")

"""Para imprimir primero la suma y luego la multiplicacion podemos hacer:
def op(num1, num2):
    suma = num1 + num2
    mul = num1 * num2
    return suma, mul

# llamamos a la función y desempaquetamos los resultados
resultado_suma, resultado_mul = op(4, 4)

print(f"La suma es: {resultado_suma}")
print(f"El producto es: {resultado_mul}")

Otra opcion seria:
def op(num1, num2):
    suma = num1 + num2
    mul = num1 * num2
    return suma, mul

print(f"La suma es: {op(4,4)[0]}, el producto es: {op(4,4)[1]}")"""