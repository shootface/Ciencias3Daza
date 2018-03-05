class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si esta vacia. """

    def __init__(self):
        """ Crea una cola vacia. """
        # La cola vacia se representa con una lista vacia
        self.items = []

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola esta vacia levanta una excepcion. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def es_vacia(self):
        """ Devuelve True si la lista esta vacia, False si no. """
        return self.items == []


if __name__ == "__main__":
    cardiacos=Cola()
    respiratorias=Cola()
    musculares=Cola()
    cardiacos.encolar("Luis")
    cardiacos.encolar("Carlos")
    cardiacos.encolar("Juan")
    respiratorias.encolar("Maria")
    respiratorias.encolar("Laura")
    menu=0
    while(menu<3):
        print "\n\t\tBienvenido al sistema de urgencias \n"
        print "1. Ingresar urgencia"
        print "2. Atender pacientes"
        print "0. salir del sistema"
        menu=input()
        if(menu==1):
            print "Sintomatologia del paciente"
            print "1. Cardiaco"
            print "2. Respiratorio"
            print "3. Muscular"
            sintoma=input()
            if(sintoma==1):
                print "Paciente con problemas cardiacos, ingrese el nombre:"
                nombre=input()
                cardiacos.encolar(nombre)
            else:
                if(sintoma==2):
                    print "Paciente con problemas respiratorios, ingrese el nombre:"
                    nombre = input()
                    respiratorias.encolar(nombre)
                else:
                    if (sintoma == 3):
                        print "Paciente con problemas musculares, ingrese el nombre:"
                        nombre = input()
                        musculares.encolar(nombre)
        if(menu==2):
            print "\t\t\tPACIENTES POR ATENDER\n\n"
            print "Pacientes con problemas cardiacos: "
            print cardiacos.items
            print "Pacientes con problemas respiratorios: "
            print respiratorias.items
            print "Pacientes con problemas musculares: "
            print musculares.items
            print "\n"
            prioridades = Cola()
            prioridades.encolar(cardiacos)
            prioridades.encolar(respiratorias)
            prioridades.encolar(musculares)
            print "Atendiendo pacientes con problemas cardiacos... \n"
            tanda1=prioridades.desencolar()
            while (tanda1.es_vacia()==False):
                print "Atendiendo al paciente "+tanda1.desencolar()
                if(tanda1.es_vacia() == True):
                    print "\nSE HAN ATENDIDO TODOS LOS PACIENTES CON PROBLEMAS CARDIACOS DE MANERA SATISFACTORIA \n\n"

            print "Atendiendo pacientes con problemas respiratorios... \n"
            tanda2 = prioridades.desencolar()
            while (tanda2.es_vacia() == False):
                print "Atendiendo al paciente " + tanda2.desencolar()
                if (tanda2.es_vacia() == True):
                    print "\nSE HAN ATENDIDO TODOS LOS PACIENTES CON PROBLEMAS RESPIRATORIOS DE MANERA SATISFACTORIA \n\n"

            print "Atendiendo pacientes con problemas musculatorios... \n"
            tanda2 = prioridades.desencolar()
            while (tanda2.es_vacia() == False):
                print "Atendiendo al paciente " + tanda2.desencolar()
                if (tanda2.es_vacia() == True):
                    print "\nSE HAN ATENDIDO TODOS LOS PACIENTES CON PROBLEMAS MUSCULARES DE MANERA SATISFACTORIA \n\n"