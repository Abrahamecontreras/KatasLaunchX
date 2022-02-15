#Ejercicio 1 
text = """On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

text_split = text.split('. ')

words = ["average", "temperature", "distance"]


for item in text_split:
   for word in words:
      if word in item:
         print(item.replace(' C', ' Celsius'))
         break


#Ejercicio 2
name = "Moon"
gravity = 0.00162 
planet = "Earth"

#planet = 'Marte '
#gravity  = 0.00143
#name = 'Ganímedes'

grav_to_m2 = gravity * 1000

title = f"""Gravity facts about {name}""".title()

data = f"""------------------------------------------------------------------------------- 
Planet Name: {planet} 
Gravity on {name} is {grav_to_m2} m/s²"""

template = f"""{title}
{data}"""

print(template)

new_template = f"""Gravity facts about {name}
------------------------------------------------------------------------------- 
Planet Name: {planet} 
Gravity on {name} is {gravity} m/s²"""

print(new_template.format(planet = planet, name = name, gravity = gravity*1000))