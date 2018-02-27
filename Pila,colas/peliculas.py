
class Cola:
 
    def __init__(self):
        self.items=[]

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def es_vacia(self):
        return self.items == []

class Pelicula:

    def __init__(self,nombre,genero):
        self.nombre=nombre
        self.genero=genero

class Genero:

    def __init__(self,nombre):
        self.nombre = nombre
        self.items=[]
    
    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def es_vacia(self):
        return self.items == []
    
generos = Cola()
while True:
    accion = int(input(" 1. Agregar pelicula \n 2. Agregar genero \n 3. Listar \n 4. Salir\n"))
    print("Accion:",accion)
    if (accion==4):
        break
    elif (accion==2):
        g1 = Genero(input("Digite el nombre del genero :"))
        generos.encolar(g1)
    elif (accion==3):
        print("HOLA")
        geT = Cola()
        while (generos.es_vacia()==False):
            temp = generos.desencolar()
            print(temp.nombre)
            geT.encolar(temp)
        while (geT.es_vacia()==False):
            temp = geT.desencolar()
            generos.encolar(temp)
    elif (accion==1):
        geB = input("Ingrese el genero de la pelicula")
        p1 = Pelicula(input("Ingrese el nombre de la pelicula"),geB)
        while (generos.es_vacia()==False):
            temp = generos.desencolar()
            if(temp.nombre==geB):
                temp.encolar()
