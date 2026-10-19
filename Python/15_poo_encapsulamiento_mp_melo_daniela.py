class Guerrero:
    nombre: str
    __poder: int

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.__poder = poder

    def get_poder(self):
        return self.__poder

vegeta = Guerrero("vegeta", 8000)
print("Guerrero: ", vegeta.nombre)
print("Poder: ", vegeta.get_poder())

class CuentaZeni:
    titular: str
    __saldo: int

    def __init__(self, titular: str, saldo: int):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def retirar_dinero(self, cantidad: int):
        if cantidad >0 and cantidad<=self.__saldo:
            self.__saldo -= cantidad
            print("Retiro realizado", cantidad)
        else:
            print("Retiro no permitido")

cuenta = CuentaZeni("Mr. Satan", 5000)
print("Titular: ", cuenta.titular)
print("Saldo inicial:", cuenta.get_saldo())
cuenta.retirar_dinero(500)
print("Saldo final", cuenta.get_saldo())

class AlmacenSemillas:
    __cantidad: int
    def __init__(self, __cantidad= int):
        self.__cantidad = __cantidad

    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, cantidad_nueva):
        if cantidad_nueva >= 0:
            self.__cantidad = cantidad_nueva
        else:
            raise ValueError ("La nueva cantidad no puede ser un numero negativo")
    
    def entregar_semillas(self, cantidad):
        if cantidad <= 0:
            print("La cantidad ingresada no pude ser negativa ")
        elif cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se entrega {cantidad} semillas")
        else:
            print(f"No hay suficientes semillas disponibles")

almacen = AlmacenSemillas(10)
almacen.entregar_semillas(3)
almacen.entregar_semillas(9)

print(f"Cantidad final disponible de semillas: {almacen.get_cantidad()}")