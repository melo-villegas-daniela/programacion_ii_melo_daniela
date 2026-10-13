# ciclo for
naves=[
    "Caza N-1",
    "Nave real de Naboo", 
    "Transporte"
]
for nave in naves:
    print("Inspeccionando", nave)

print("Inspeccion realizada")

rondas = range(1,6)

print("Tipo de Rondas:" , type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia {ronda}")
    print (f"Tipo de datto ronda: {type(ronda)}")

droides = range(1,17,3)

print("Tipo de droides:", type(droides))
for droide in droides:
    print(f"Reparar : droide B1-{droide}")
    print(f"Tipo de dato droide: {type(droide)}")

planetas=[
    "Naboo", 
    "Tatooine", 
    "Coruscant",]

recorrido = enumerate (planetas, start=5)

for posicion, planeta in recorrido:
    print(f"Destino {posicion}: {planeta}")
    print(f"Tipos de dato {type(posicion)}: {type(planeta)}")

paises = [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brazil",
    "Estados Unidos"
]

for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brazil":
        break
    print(f"Pais visitado: {pais}")

jedi = {}
jedi_activo = {
    "nombre": "Obiwan",
    "fuerza": "120",
    "estilo_pelea": "samurai",
    "misiones": ["guerra alderan", "secuestro palpatine","escolta de leia "],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}
print(jedi_activo)
nave = dict(nombre="AZ-1", capacidad= 8, turbo_lazer=2 )
print(nave)

jedi["nombre"] = "Luck"
jedi["fuerza"] = 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave} - {valor}")