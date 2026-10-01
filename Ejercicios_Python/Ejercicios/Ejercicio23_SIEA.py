#23. Crea una jerarqu´ıa de clases Persona ⇒ Empleado ⇒ Jefe donde Persona tiene los atributos nombre
#y edad (y los m´etodos para obtenerlos), Empleado a˜nade el atributo sueldo, y Jefe es un empleado
#con un sueldo prefijado. Todos los atributos deben ser privados.


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre# __ significa que es un atributo privado
        self.__edad = edad

    def mostrar_nombre(self):
        print(f"Mi nombre es: {self.__nombre}")

    def mostrar_edad(self):
        print(f"Mi edad es de {self.__edad} años")

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):#Inicializamos con lo que ya tenia el padre mas el atributo nuevo, ponemos sueldo pq se lo pasaremos por parametro
        super().__init__(nombre, edad)#Inicializamos con lo que ya tenia el padre es decir clase persona
        self.__sueldo = sueldo#Añadimos el nuevo atributo
    def mostrar_sueldo(self):
        print(f"El sueldo es: {self.__sueldo}€")

class Jefe (Empleado):
    def __init__(self, nombre, edad):#inicializamos con lo que tenia el padre, no ponemos el parametro de sueldo pq sera un sueldo ya fijado
        sueldo = 3000
        super().__init__(nombre, edad, sueldo)#se inicializa con lo que tiene la clase empleado


print("---- PERSONA ----")
mi_persona = Persona("Luis", 18)
mi_persona.mostrar_nombre()
mi_persona.mostrar_edad()
print()

print("---- EMPLEADO ----")
mi_empleado = Empleado("Lolo", 20, 1000)
mi_empleado.mostrar_nombre()
mi_empleado.mostrar_edad()
mi_empleado.mostrar_sueldo()
print()

print("---- JEFE ----")
mi_jefe = Jefe("Jose", 40)
mi_jefe.mostrar_nombre()
mi_jefe.mostrar_edad()
mi_jefe.mostrar_sueldo()