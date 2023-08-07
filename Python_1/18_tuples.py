numbers = (1, 2, 3, 4, 5)
strings = ('nico', 'zule', 'santi', 'nico')

print(numbers)
print(' 0 =>', numbers[0])
print(' 0 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD 
# Tupla solo se da la declaracion, no se puede modificar como los CRUD

'''
Esto no se permite en las tuplas
numbers.append(10)
print(numbers)

numbers[1] = 'Change
print(numbers)
'''

print(strings)
print(strings.index('zule'))

print(strings.count('nico'))

#convertir a lista
my_list = list(strings)

print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

#convertir lista a tuple
my_tuple = tuple(my_list)
print(my_tuple)