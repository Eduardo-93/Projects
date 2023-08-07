numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'Hola']
print(types)

print(numbers[0])
print(tasks[0])

#No es valido
text = 'Hola'
#text[0] = 'w'

#Esto es una mutacion, solo se puede hacer en listas
tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3]) #Selecciona los numeros desde el inicio hasta la posicion 3
print(True in types)
print('Hola' in types)