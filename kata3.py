#ejercicio 1
vel_asteroide = 49

if vel_asteroide > 25:
   print("Advertencia, un asteroide se aproxima a la tierra a " + str(vel_asteroide ) + " km por segundo")
else:
   print("Todo bajo control")

#ejercicio 2
vel_asteroide2 = 19

if vel_asteroide2 > 20:
    print('Un asteroide ha entrado en la órbita de la tierra, mira al cielo y busca una luz brillante!')
elif vel_asteroide2 == 20:
    print('Un asteroide ha entrado en la órbita de la tierra, mira al cielo y busca una luz brillante!')
else:
    print('Otro día normal')

#ejercicio 3
dim_asteroide = 20
vel_asteroide3 = 21

if (dim_asteroide > 25 and vel_asteroide > 25):
   print("Mensaje: asteroide de " + str(dim_asteroide) + " m de diámetro se aproxima a la tierra a una velocidad de " + str(vel_asteroide) + " KM por segundo" )
elif(dim_asteroide < 25):
   print("Asteroide de " + str(dim_asteroide) +  " m de diámetro con curso de colisión a la tierra no causará ningún peligro ya que se desintegrará debido a su tamaño")
elif(vel_asteroide3 >= 20):
   print("Un asteroide ha entrado en la órbita de la tierra, mira al cielo y busca una luz brillante!")      
else: print("Todo bajo control")
