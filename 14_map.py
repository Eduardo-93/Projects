#MAP ES MUY IMPORTANTE. APRENDERLO BIEN

numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2) #esto es una transformacion

#Con lambda y map
numbers_v3 = list(map(lambda i: i*2, numbers))

print(numbers_v3, '\n')

#Iterar dos listas y dar una transformacion de ellas
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2, '\n')
result = list(map(lambda x, y: x + y, numbers_1, numbers_2)) #Suma las dos listas sin dar resultado del elemento 4 ya que solo esta ese elemento en una lista
print(result)
