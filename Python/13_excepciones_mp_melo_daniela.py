print("==== CONTROL DE ENERGIA ====")
energia_texto = "ochenta"
try:
    energia = int("mucho")
    print(energia)
except ValueError:
    print("Error: debe ser numerico")

print("Fin del sistema")

"""
No Especifica en except captura todos errores
ValueError
TypeError
KeyError --> Diccionario
IndexError --> Indice arreglo no exite
ZeroDivisionError --> algo entre cero
"""


def calcular_energia(total, cantidad):
    try:
        resultado = total/cantidad
        return resultado
    except ZeroDivisionError as error:
        print("Error: division entre cero", error)
    except TypeError:
        print("Error: valores deben ser numericos")

print("Caso 1:", calcular_energia(100,4))
print("Caso 2:", calcular_energia(100,0))
print("Caso 1:", calcular_energia(100,"cuatro"))

print("========DIAGNOSTICO R2-D2========")
try:
    energia = int("cuatro")
    print("energia", energia)
except ValueError:
    print ("Error de lectura")
else:
    print("diagnostico completado")
finally:
    print("Cerrando diagnostico")

def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser numero entero")
    if energia <0 or energia>100:
        raise ValueError("La energia debe ser entre 0 y 1000")
    return energia
try:
    resultado = validar_energia(60)
    print("Energia", resultado)
except (TypeError,ValueError) as error:
    print("Error", error)