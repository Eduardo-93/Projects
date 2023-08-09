import sys
print(sys.path, '\n')

import re
text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text) # Dentro del texto solo guardo los numeros del 0 al 9 mas otras coincidencias
print(result, '\n')

#Importa la hora en formato digital
import time
timestamp = time.time()
print(timestamp)

#Convertirlo a horario entendible
local = time.localtime()
result = time.asctime(local)
print('\n', result) 

import collections
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers) # Guarda la frecuencia en la que se repiten los numeros y los guarda en la variable counter
print('\n', counter) # Imprime la cantidad de veces que se repitio un numero