#Ejercicio 1: Trabajar con argumentos en funciones

def check_tanks(tank1, tank2, tank3):
   prom = avg(tank1, tank2, tank3)
   return f'''Tank 1: {tank1}, Tank 2: {tank2}, Tank 3: {tank3}
Average: {prom}'''

def avg(*args):
    sumData = 0
    for data in args:
        sumData = sumData + data
    average = sumData / len(args)
    return average


print(check_tanks(20, 15, 12))

#Ejercicio 2: Trabajo con argumentos de palabra clave

def mission_report(destination, *minutes, **fuel_reservoirs):
    sumMinutes = sum(minutes)
    report = f"""
    Destination: {destination}
    Travel time: {sumMinutes}
    Fuel: {sum(fuel_reservoirs.values())}
    """

    for tank, liters in fuel_reservoirs.items():
        report += f"{liters} in {tank}\n"
    return report

print(mission_report("Moon", 10, 12, 17, internal=30, external=20))