#Ejercicio 1: Creación de un bucle "while"
new_planet = ''

planets = []

while new_planet.lower() != 'done':
    if(new_planet):
        planets.append(new_planet)
    new_planet = input('Type a new name of a planet or "done" when done')
#Ejercicio 2: Creación de un bucle "for"
for planet in planets:
    print(planet)


