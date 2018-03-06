class Pila:
        def __init__(self):
            """ Crea una pila vacia. """
            # La pila vacia se representa con una lista vacia
            self.items=[]

        def apilar(self, x):
            """ Agrega el elemento x a la pila. """
            # Apilar es agregar al final de la lista.
            self.items.append(x)

        def desapilar(self):
            """ Devuelve el elemento tope y lo elimina de la pila.
                Si la pila esta vacia levanta una excepcion. """
            try:
                return self.items.pop()
            except IndexError:
                raise ValueError("La pila esta vacia")

        def es_vacia(self):
            """ Devuelve True si la lista esta vacia, False si no. """
            return self.items == []

        def operacion(self, operador, num1, num2):
            if operador == "+":
                return int(num2) + int(num1)
            else:
                if operador == "-":
                    return int(num2) - int(num1)
                else:
                    if operador == "*":
                        return int(num2) * int(num1)
                    else:
                        if operador == "/":
                            if int(num1)==0:
                                return "nop"
                            else:
                                return int(num2) / int(num1)

def letra(a):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if a in mayusculas:
        return 1
    else:
        return 0

def verificarOperadores(cadena):
    datos=cadena.split(" ")
    #print(datos) 
    while len(datos)+1!=0:
        if len(datos)!=0:
            try:
                int(datos[0])
                datos.pop(0)
            except ValueError:
                if datos[0]=="+" or datos[0]=="-" or datos[0]=="*" or datos[0]=="/":
                    datos.pop(0)
                else:
                    if letra(datos[0]):
                        if len(datos)==2:
                            return 1
                        else:
                            return 0
                    else:
                        #print(datos[0])
                        #print("Error Estructura")
                        return 0
        else:
            #print("todo ultra")
            return 1

def verificarSintaxis(cadena):
    datos=cadena.split(" ")
    obj=Pila()
    for dato in datos:
        if dato == "+" or dato == "-" or dato == "*" or dato == "/":
            num1 = obj.desapilar()
            num2 = obj.desapilar()
            try:
                resultado = obj.operacion(dato, num1, num2)
            except ValueError:
                #print "error en las operaciones" 
                return 0           
            obj.apilar(resultado)
        else:
            obj.apilar(dato)
    if len(obj.items)!=3:
        return 0
    else:
        return 1
 
def lecturaDatos(nombre):
    operaciones = Pila()
    oper = []
    archivo = open(nombre,"r")
    for linea in archivo.readlines():
        #print type(linea)
        #print linea
        operaciones.apilar(linea)
    archivo.close()
    return operaciones

def verificar(archivo):
    operaciones = lecturaDatos(archivo)
    while operaciones.es_vacia()==False:
        leido = operaciones.desapilar()
        if verificarOperadores(leido):
            if verificarSintaxis(leido):
                print("BIEN SINTAXIS",leido)
            else:
                print("MAL SINTAXIS",leido)
        else:
            print("MAL OP",leido)



verificar("verificar.txt")
#print("operador",verificarOperadores("X 3 5 % ="))