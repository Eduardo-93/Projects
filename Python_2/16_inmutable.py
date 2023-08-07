items = [
    {
        'Product': 'Camisa',
        'Price': 100,
    },
    {
        'Product': 'Pantalones',
        'Price': 300,
    },
    {
        'Product': 'Pantalones 2',
        'Price': 200,
    }
]

def add_taxes(item):
    new_item = item.copy() #Este copy sirve para crear una copia con la cual trabajar sin necesidad de modificar el array original, asi los cambios que se hagan en uno no se vean afectados en el otro
    new_item['Taxes'] = new_item['Price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('\nOld list')
print(items)