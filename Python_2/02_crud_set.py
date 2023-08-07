set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries) #Esta dentro del conjunto
print('pe' in set_countries) #No esta dentro del conjunto

# Add, se sigue respetando la condicion de no repetidos aun se agregue de forma manual
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# Update
set_countries.update({'ar', 'ecua', 'pe'}) # Agrega ar y ecua, pe no lo agrega porque es repetido
print(set_countries)

# Remove
set_countries.remove('col') #Se elimino col del conjunto
print(set_countries)
#set_countries.remove('arg') #Si se intenta eliminar un elemento que no existe dentro del conjunto da error y cierra programa
#print(set_countries)
set_countries.discard('arg') #Si no se encuentra el elemento dentro del conjunto no pasa nada
print(set_countries)
print(len(set_countries))
set_countries.clear() #Elimina todos los elementos guardados en el conjunto
print(set_countries)
print(len(set_countries))