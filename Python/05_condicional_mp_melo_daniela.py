# Condicional if
# Simple

combustible = 5
if combustible >= 10:
    print("Puedes despegar")

# Condicional if-else
creditos = int(input("Ingresa la cantidad de creditos que tienes: "))
precio_repuesto = int(input("Ingresa el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

# if anidado
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobran creditos")
    else:
        print("Te quedas justo con los creditos necesarios")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

# Condicional if-elif-else
if creditos > precio_repuesto:
    print("Puedes comprar el repuesto y te sobran creditos")
elif creditos == precio_repuesto:
    print("Puedes comprar el repuesto y te quedas justo con los creditos necesarios")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

# Condicional if-elif-else
tipo_repuesto = input("Ingresa el tipo de repuesto motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "ala":
    print("Puedes comprar el repuesto y te sobran creditos")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobrajn creditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran creditos")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

precio = 0
total = 0

peso_paquete = float(input("Ingrese el peso del paquete en kg(puede tener decimales):"))

print("Zonas de destino:")
print("1. America")
print("2. Europa")
print("3. Resto del mundo")
zona_destino = int(input("Dependiendo de su zona de destino, ingrese el numero correspondiente:" ))
if zona_destino == 1:
    precio = 5
    total = precio * peso_paquete
elif zona_destino == 2:
    precio = 7.5
    total = precio * peso_paquete
elif zona_destino == 3:
    precio = 10
    total = precio * peso_paquete
else: 
    print(" El destino que escogiste no esta disponible")

print ("El precio total del envio es de: ", total)