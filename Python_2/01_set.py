# IMPORTANTE no imprime elementos repetidos

set_countries = {'col', 'mex', 'bol', 'bol'} #No acepta elementos duplicados
print(set_countries) #no imprime el segundo bol ya que esta repetido
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'Hola', False, 12.12}
print(set_types) #Al imprimir cambia el orden del SET, pero no afecta en nada

set_from_string = set('hola') #convierte un conjunto(set) de un string
print(set_from_string) #reparte cada uno de los caracteres de Hola y los separa en un set

set_from_tupla = set(('abc', 'cbv', 'as', 'abc')) #Convierte una dupla en un conjunto
print(set_from_tupla) 

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers) #convierte el set de numeros en una lista(array) sin los duplicados
print(unique_numbers) 