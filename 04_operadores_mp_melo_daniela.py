#Operadores
"""
Operadores aritmeticos:
- + (suma)
- - (resta)
- * (multiplicacion)
- / (division)
- % (modulo)
- ** (potencia)
"""
valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Modulo:", modulo)
print("Potencia:", potencia)

print("Tabla de multiplicar del 5")
multiplicador = 5
print("multiplicador x 1 =", multiplicador  * 1)
print("multiplicador x 2 =", multiplicador  * 2)
print("multiplicador x 3 =", multiplicador  * 3)
print("multiplicador x 4 =", multiplicador  * 4)
print("multiplicador x 5 =", multiplicador  * 5)
print("multiplicador x 6 =", multiplicador  * 6)
print("multiplicador x 7 =", multiplicador  * 7)
print("multiplicador x 8 =", multiplicador  * 8)
print("multiplicador x 9 =", multiplicador  * 9)
print("multiplicador x 10 =", multiplicador  * 10)

print("Area de un triangulo con base 5 y la altura 10:", (5 * 10) / 2)

#Operadores de comparacion
"""
- == (igual)
- != (distinto)
- > (mayor que)
- < (menor que)
- <= (mayor o igual que)
- >= (menor o igual que)
"""

velocidad_anakin = 950
velocidad_sebulba = 100

print("¿Anakin es mas rapido que sebulba?", velocidad_anakin > velocidad_sebulba)
print("¿Anakin es mas lento que sebulba?", velocidad_anakin < velocidad_sebulba)
print("¿Anakin es igual de rapido que sebulba?", velocidad_anakin == velocidad_sebulba)

#Operadores logicos
"""
- and (y)
- or (o)
- not (no)
"""

motores_funcionando = True
escudos_funcionando = False
combustible = 80

print("¿Todos los sistemas estan funcionando?", motores_funcionando and escudos_funcionando)
print("Algunos sistemas estan funcionando?", motores_funcionando or escudos_funcionando)
print("¿Los motores no estan funcionando?", not motores_funcionando)

cantidad_motores = 2
cantidad_alas = 4
combustible = 80

print( "¿La nave tiene 2 motores y 4 alas?")
print(cantidad_motores >= 2 and cantidad_alas >= 4 and combustible >= 50)
print("¿La nave tiene 2 motores o 4 alas?")
print(cantidad_motores >= 2 or cantidad_alas >= 4 or combustible >= 50)
print("¿La nave no tiene al menos 2 motores?")
print(not cantidad_motores >= 2 and combustible > 50 and cantidad_alas >= 4)

#Operadores de asignacion
"""
- = (asignacion)
- += (suma y asignacion)
- -= (resta y asignacion)
- *= (multiplicacion y asignacion)
- /= (division y asignacion)
- %= (modulo y asignacion)
- **= (potencia y asignacion)
"""

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad despues de acelerar 50:", velocidad)
velocidad -= 30
print("Velocidad despues de frenar 30:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad despues de multiplicar:", velocidad)
divisior = 4
velocidad /= divisior
print("Velocidad despues de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad despues de aplicar modulo:", velocidad)
velocidad **= 2
print("Velocidad despues de aplicar potencia:", velocidad)

#Precencia de operadores
"""
1. ()
2. ** (potencia)
3. * / % (multiplicacion, division, modulo)
4. + - (suma, resta)
"""

resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)
resultado_3 = 10 + 5 * 2 ** 2
print("Resultado 3:", resultado_3)