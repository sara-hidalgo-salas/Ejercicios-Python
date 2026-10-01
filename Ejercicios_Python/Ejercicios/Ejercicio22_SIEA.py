#22. Crea una clase “contador” que admita un valor inicial y un rango de valores extremos (menor,mayor).
#Si el valor inicial est´a fuera del rango dado se reasignar´a el valor inicial al m´as cercano de los extremos.
#Se definir´an dos m´etodos “incrementa” y “decremeta” que realizar´an las operaciones indicadas pero
#manteniendo el contador dentro del rango. Por defecto el incremento ser´a de 1 salvo que se pase por
#par´ametro un valor distinto

#Clase
class contador: 
    def __init__(self, valor_inicial, menor, mayor):#el valor inicial es el valor del contador
        #Atributos
        self.valor_inicial = valor_inicial
        self.menor = menor
        self.mayor = mayor

        print(f"El valor inicial es: {self.valor_inicial}")
        if self.valor_inicial < self.menor or self.valor_inicial > self.mayor:#si se cumple uno solo es OR, si se cumplen los dos AND
            print("El valor inicial esta fuera del rango")#para que sea fuera del rango uno debe ser menor que 0 y el otro mayor a 10 como no se pueden cumplir los dos a la vez es un or
            if self.valor_inicial < self.menor:
                self.valor_inicial = self.menor#guardamos el nuevo valor
                print(f"El nuevo valor mas cercano del valor inicial es: {self.valor_inicial}")

            elif self.valor_inicial > self.mayor :
                self.valor_inicial = self.mayor#guardamos el nuevo valor 
                print(f"El nuevo valor mas cercano del valor inicial es: {self.valor_inicial}")  

        #Esta opcion de ahora va a ser utilizando la media
            """media = (self.menor + self.mayor)/2
            if self.valor_inicial < media:
                self.valor_inicial = self.menor
                print(f"ahora el valor inicial es: {self.valor_inicial}")

            elif self.valor_inicial > media :
                self.valor_inicial = self.mayor
                print(f"ahora el valor inicial es: {self.valor_inicial}")"""
             
        elif self.valor_inicial >= self.menor and self.valor_inicial <= self.mayor:#esta dentro del rango y es and porque se deben cumplir los dos para que este dentro del rango:
            print("El valor inicial esta dentro del rango") #para que este dentro del rango debe ser entre 0 y 10 por lo que se debe cumplir que uno sea mayor que 0 y el otro menor que 10
    

    def Incrementa(self, num_sum=1):#num_sum=1 para pasarle por defecto 1
        nuevo_valor = self.valor_inicial + num_sum 
        print(f"El valor del incremento es: {nuevo_valor}")
        #comprobamos si el nuevo valor esta fuera del rango
        if nuevo_valor < self.menor:
            nuevo_valor = self.menor
            print(f"Como el nuevo valor al incrementarlo esta por debajo del rango su nuevo valor mas cercano es: {nuevo_valor}")
        elif nuevo_valor > self.mayor:
            nuevo_valor = self.mayor
            print(f"Como el nuevo valor al incrementarlo esta por encima del rango su nuevo valor mas cercano es: {nuevo_valor}")
        self.valor_inicial = nuevo_valor #guardamos su valor actual despues de incrementarlo


    def Decrementa(self, num_rest=1):
        nuevo_valor = self.valor_inicial - num_rest#pensar que el valor inicial es el ultimo que se ha quedado al hacer el incremento 
        print(f"El valor del decremento es: {nuevo_valor}")
        #comprobamos si el nuevo valor esta fuera del rango
        if nuevo_valor < self.menor:
            nuevo_valor = self.menor
            print(f"Como el nuevo valor al decrementarlo esta por debajo  del rango su nuevo valor mas cercano es: {nuevo_valor}")
        elif nuevo_valor > self.mayor:
            nuevo_valor = self.mayor
            print(f"Como el nuevo valor al decrementarlo esta por encima  del rango su nuevo valor mas cercano es: {nuevo_valor}")
        self.valor_inicial = nuevo_valor #guardamos su valor actual despues de incrementarlo

mi_contador = contador(10, 0, 10)#Objeto
#print (mi_contador.valor_inicial)
mi_contador.Incrementa()
mi_contador.Decrementa()