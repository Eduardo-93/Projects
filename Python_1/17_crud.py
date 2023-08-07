#Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5] #Crear
print(numbers[1]) #Leer
numbers[-1] = 10 #Acualizar
print(numbers)

numbers.append(700) #Agrega un nuevo elemento a la lista
print(numbers)

numbers.insert(0, 'Hola') # Agrega un nuevo elemento en la posicion 0, el elemento es Hola
print(numbers)

numbers.insert(3, 'change') # Agrega un elemento en la posicion 3, el elemento es change
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo3']
new_list = numbers + tasks #Fuciona la lista de numbers y tasks y los guarda en la nueva lista new_list
print(new_list)

print(new_list.index('todo 2')) #En que posicion esta el elemento todo 2
index = new_list.index('todo 2') #ubica la posicion de todo 2 en la lista y lo guarda en index
new_list[index] = 'todo changed' #Cambia el todo 2 a todo changed 
print(new_list)

new_list.remove('todo 1') #Elimina el elemento todo 1 de la lista
print(new_list)

new_list.pop() #Elimina el ultimo elemento de la lista
print(new_list)

new_list.pop(0) #Elimina el elemento en la posicion 0, en este caso es Hola
print(new_list)

new_list.reverse() #Voltea la lista
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort() #Ordena automaticamente los elementos de menor a mayor
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort() #Ordena tambien de menor a mayor en base la primer letra
print(strings)

# new_list.sort() En este caso no lo ordena ya que son varios tipos de datos en una sola lista