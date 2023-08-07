"""
for element in range(1, 21):
    print(element)

"""

my_list = [23, 45, 67, 89, 43]

for i in my_list:
    print(i)

my_tuple = ('nico', 'juli', 'santi')
for i in my_tuple:
    print(i)

product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}
for key in product:
    print(product[key]) # Si solo coloco key, me dara solo name, price y stock del diccionario

for key, value in product.items():
    print(key, '=>', value)

#lista con diccionario
people = [
    {
        'name': 'nico',
        'age': 29
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

for person in people:
    print('Name: ', person['name'], '-> Age:', person['age'])