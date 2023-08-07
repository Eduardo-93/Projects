import random
countries = ['col', 'mex', 'bol', 'pe']
population = { country: random.randint(1,100) for country in countries }
print(population)

result = { country: population for (country, population) in population.items() if population > 20 }
print(result)

text = 'Hola, soy Eduardo'
text_v2 = text.lower()
unique = { c: c.upper() for c in text_v2 if c in 'aeiou' }
print(unique)