# string -> cadena de texto
my_name = "Eduardo"
my_name = 'Solorio'

print('my_name =>', my_name)
print(type(my_name))

# Enteros => numeros enteros

my_age = 29

print(my_age)
print(type(my_age))

# Booleans -> Falso o Verdadero

is_single = True
print(is_single)
is_single = False
print(is_single)
print(type(is_single))

# Siempre se toma una cadena de texto cuando se usa input, ya sea solo numeros, o lo que sea.
my_age = input("Cual es tu edad? ")
print('my_age', my_age)
print(type(my_age))

"""
~~ Tipos de datos primitivos ~~
Integers: números Enteros
Floats: números de punto flotante (decimales)
Strings: cadena de caracteres (texto)
Boolean: boolenaos (Verdadero o Falso)

~~ Tipos de dato adicionales ~~
Datos en texto: str
Datos numéricos: int, float, complex
Datos en secuencia: list, tuple, range
Datos de mapeo: dict
Set Types: set, frozenset
Datos booleanos: bool
Datos binarios: bytes, bytearray, memoryview
"""