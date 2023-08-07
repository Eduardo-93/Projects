my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'blablabla',
    'name': "Eduardo",
    'last_name': "Solorio",
    'age': 29
}

print(my_dict)
print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name']) #Si se usa este metodo y no hay un valor en el diccionario, da error
print(my_dict.get('valor')) #Cuando se usa get te da un valor nulo cuando el valor no existe en el diccionario
print('avion' in my_dict)
print('otroqueno' in my_dict)