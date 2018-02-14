class Cola:
    def __init__(self):
        self.items=[]
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")
    def es_vacia(self):
        return self.items == []
    def recorrer
class nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der
class arbolBinario:
    def __init__(self):
        # inicializa la raiz
        self.raiz = None
 
    def agregarNodo(self, dato):
        # crea un nuevo nodo y lo devuelve
        return nodo(dato)
 
    def insertar(self, raiz, dato):
        # inserta un dato nuevo en el árbol
        if raiz == None:
            # si no hay nodos en el árbol lo agrega
            return self.agregarNodo(dato)
        else:
            # si hay nodos en el árbol lo recorre
            if dato <= raiz.dato:
                # si el dato ingresado es  menor que el dato guardado va al subárbol izquierdo
                raiz.izq = self.insertar(raiz.izq, dato)
            else:
                # si no, procesa el subárbol derecho
                raiz.der = self.insertar(raiz.der, dato)
            return raiz
class Pelicula:
    nombre=0
    genero=0

class Genero:
    nombre=0
    peliculas = Cola()

    def agregarPelicula(pelicula):
        if pelicula.genero==self.nombre:
            peliculas.encolar(pelicula)
        else:
            print ("La pelicula no corresponde a ese genero")
        
class Organizar:
    generos = arbolBinario()

    def agregarGenero(genero):
        generos.
    
def main():
    gaccion = Genero()
    gaccion.nombre="Accion"
    pTerminator = Pelicula()
    pTerminator.genero="Accion"
    pTerminator.nombre="Termineitor1"
    org =  Organizar()
    org.agregarGenero(gaccion) 


