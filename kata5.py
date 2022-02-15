#Ejercicio1 - Utilizar operadores aritméticos

distance_earth = 149597870
distance_jupyter = 778547200

distance_btwn = distance_jupyter - distance_earth

distance_btwnM = distance_btwn * 0.621 #la solución usa un dato distinto, revisar

print(distance_btwn)

print(distance_btwnM)

#Ejercicio 2: convierte cadenas en números y usa valores absolutos

#Planeta	Distancia al sol

#Mercurio	57900000
#Venus	   108200000
#Tierra	   149600000
#Marte	   227900000
#Júpiter	   778600000
#Saturno	   1433500000
#Urano	   2872500000
#Neptuno	   4495100000

first_planet = input("Ingrese la distancia del primer planeta al sol")
second_planet = input("Ingrese la distancia del segundo planeta al sol")

first_planet =  int(first_planet)
second_planet = int(second_planet)

distance_in_km = second_planet - abs(first_planet)
distance_in_m = distance_in_km * 0.621

print(distance_in_km)
print(distance_in_m)
