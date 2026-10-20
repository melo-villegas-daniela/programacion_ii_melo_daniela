class Guerrero:
    nombre: str
    poder: int
    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.poder = poder

    def saludar(self):
        print("Hola, soy :", self.nombre)

    def entrenar(self):
        aumento = 200
        self.poder += aumento 

    def atacar(self, cantidad):
        danio = self.poder*cantidad
        print("Guerrero", self.nombre)
        print("Daño causado: ", danio)

goku = Guerrero("Goku", 9000)

goku.saludar()

print("Nombre del personaje:", goku.nombre)
print("Poder del personaje:", goku.poder)
goku.entrenar()
print("Poder del personaje:", goku.poder)
goku.atacar(2)


class RadarDragon:
    region1: int
    region2: int

    def __init__(self, region1:int, region2:int):
        self.region1 = region1
        self.region2 = region2


    def buscar_esferas(self):
        esferas_encontradas = self.region1 + self.region2
        esferas_faltantes = 7 - esferas_encontradas
        print("Esferas encontradas:", esferas_encontradas)
        print("Esferas que faltan:", esferas_faltantes)

radar_bulma = RadarDragon(3,2)
radar_bulma.buscar_esferas()

