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

prices = list(map(lambda item: item['Price'], items))
print(items)
print(prices, '\n')

def add_taxes(item):
    item['Taxes'] = item['Price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)