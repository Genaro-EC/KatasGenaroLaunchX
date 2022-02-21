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

numlunas = planet_moons.values()

totplanetas = len(planet_moons.keys())

totlunas = 0
for luna in numlunas:
    totlunas = totlunas + luna

promedio = totlunas / totplanetas
print (promedio)