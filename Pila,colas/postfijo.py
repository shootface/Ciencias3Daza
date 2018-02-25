class Pila:
    def apilar(self, lista, x):
        lista.append(x)

    def desapilar(self, arreglo):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila esta vacia levanta una excepcion. """
        try:
            return arreglo.pop()
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
                        return int(num2) / int(num1)


if __name__ == "__main__":
    print "Ingrese la expresion"
    expresion = input()
    listaEntrada = expresion.split(" ")
    pila = []
    obj=Pila()
    for dato in listaEntrada:
        if dato == "+" or dato == "-" or dato == "*" or dato == "/":
            num1 = obj.desapilar(pila)
            num2 = obj.desapilar(pila)
            resultado = obj.operacion(dato, num1, num2)
            obj.apilar(pila, resultado)

        else:
            obj.apilar(pila, dato)
    print pila
