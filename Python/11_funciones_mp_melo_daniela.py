## FUNCIONES
# Funciones sin parametros o simples
def activar_sistema():
    print("== sistema de naboo")
    print("Sistema de control activado")

activar_sistema()

#Funciones con parametros

def saludar_jedi(nombre):
   print(f"Que la fuerza te acompañe: {nombre}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave(nombre, combustible):
   print(f"nave: {nombre}")
   print(f"cantidad combustible: {combustible}")

mostrar_nave("Caza N-1", 80)

#Funciones que devuelven datos o informacion
#Return
def calcular_combustible(inicial, consumo):
   restante = inicial - consumo
   return restante

resultado = calcular_combustible(100, 25)
print(f"Combustible:{resultado}")

def calcular_combustible2(inicial, consumo):
   return inicial-consumo

print(f"Combustible:{calcular_combustible2(100,15)}")

def nave_preparada(combustible):
   return combustible>=50

if nave_preparada(800):
   print("Nave autorizada para despegar")
else:
   print("Nave necesita recarga")

