from poo_guerrero import Guerrero
class Sayajin(Guerrero):
    def __init__(self, nombre):
        super().__init__(nombre)

    def transformarse(self):
        print(self.nombre, "se transforma en Supersayajin")

goku= Sayajin("Goku")
goku.presentarse()
goku.transformarse()