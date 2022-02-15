#Ejercicio 1: Creación de diccionarios de Python
planet = {
    'name': 'Mars',
    'moons': 2
}

print(planet['name'], "has a total of",  planet['moons'], "moons")

planet['polar'] =  6752
planet['equatorial'] = 6792

print("The polar circumference of",  planet['name'], "is :", planet['polar'])


#Ejercicio 2: Programación dinámica con diccionarios
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
planets = planet_moons.keys()

print(moons)

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

prom = total_moons / len(planets)

print(prom)