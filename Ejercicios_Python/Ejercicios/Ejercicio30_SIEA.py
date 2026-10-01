#30. Utiliza reduce para obtener el producto de todos los elementos de una lista

#A partir de Python 3 reduce no está integrada en el espacio de nombres global y debe importarse desde el módulo functools.
from functools import reduce
def mul(x, y):
    return x * y
l = [1, 2, 3, 4]
l2 = reduce(mul, l)
print(l2)


"""Otra manera de importar:
import functools
def mul(x, y):
    return x * y
l = [1, 2, 3, 4]
l2 = functools.reduce(mul, l)
print(l2)"""