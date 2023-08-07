dict = {}
for i in range(1,6):
    dict[i] = i * 2
print(dict)

dict_v2 = {i: i * 2 for i in range(1 , 6)} #diferente sintaxis a dict pero es lo mismo
print(dict_v2)

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100) #Random.randint(1,100) da un valor aleatorio de 1 a 100
print(population)

population_v2 = { country:random.randint(1,100) for country in countries}
print(population_v2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages))) #une las dos listas con zip y se convierte a una lista con list
new_dict = { name: age for (name, age) in zip(names,ages) } #Crea un dictionary a partir de las dos listas names y ages, uniendolas con zip y pasando por cada elemento de la lista con un for
print(new_dict)
