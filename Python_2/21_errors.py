#print(0 / 0)
#print(result)
print('Hola\n')

suma = lambda x, y: x + y
assert suma(2, 2) == 4

print('Hola 2\n')

age = 10
if age < 18:
    raise Exception('No se permiten menores de edad') # De esta forma creas un error, cuando no se cumpla los requisitos