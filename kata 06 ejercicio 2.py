planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
planeta= input ('Ingresa el nombre del planeta (la primera letra debe ser mayúscula): ')
lista = planetas.index(planeta)
print('los más cercanos al sol son: ' + planeta)
print(planetas[0:lista])
print('los más lejanos al son son: ' + planeta)
print(planetas[lista + 1:])
