person = {
    'name': 'Eduardo',
    'last_name': 'Solorio',
    'langs': ['python', 'javascript'],
    'age': 29
}

print(person)

person['name'] = 'Santi'
person['age'] -= 9
person['langs'].append('rust')
print(person)

del person['last_name'] #Elimina el atributo last_name del diccionario, aqui si no tiene last_name marcara valor nulo
person.pop('age') #Tambien es una forma de eliminar un atributo, aqui se tiene que colocar la llave existente que se eliminara
#pop se necesita poner de forma obligatoria lo que se eliminara

print(person)
print('items')
print(person.items()) #

print('keys')
print(person.keys())

print('values')
print(person.values())