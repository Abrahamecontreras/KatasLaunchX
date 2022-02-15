#Ejercicio 1: Crear y usar listas de Python

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Neptuno"]

print("El número de planetas que hay en el sistema solar es: ", len(planetas))

planetas.append("Plutón")

print("Antes se consideraban ", len(planetas),  "planetas en el sistema solar")

#Ejercicio 2: Trabajando con datos de una lista

planetas2 = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

usrInput = input(print("Hola, por favor ingrese el nombre de un planeta comenzando con la primera letra en Mayúscula"))

posPlaneta = planetas2.index(usrInput)

if(planetas2.index(usrInput)):
   print("Los planetas más cercanos al sol a partir de", usrInput, "son", planetas2[0:posPlaneta])
   print("Los planetas más alejados del sol a partir de", usrInput, "son", planetas2[posPlaneta + 1:])    
else:    
   print("Su planeta no se encuentra en el sistema solar")
