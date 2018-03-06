from pila import Pila

def verificarOperadores(cadena):
    datos=cadena.split(" ")
    print(datos) 
    while len(datos)+1!=0:
        if len(datos)!=0:
            try:
                print(int(datos[0]),)
                datos.pop(0)
            except ValueError:
                if datos[0]=="+" or datos[0]=="-" or datos[0]=="*" or datos[0]=="/":
                    print("todo bien")
                    datos.pop(0)
                else:
                    print("Error en los operadores")
                    return 0
        else:
            print("todo ultra")
            return 1

def verificarSintaxis(cadena):
    datos=cadena.split(" ")
    obj=Pila()
    
def lecturaDatos(nombre):
    operaciones = Pila()
    archivo = open(nombre,"r")
    for linea in archivo.readlines():
        print linea
        operaciones.apilar(linea)
    archivo.close()


lecturaDatos("verificar.txt")
#print("operador",verificarOperadores("5 7 + 7 8 + 1 4 /"))