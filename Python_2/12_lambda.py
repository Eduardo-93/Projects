def increment(x):
    return x + 1

# lambda es una funcion con una sintaxis mas corta, primero x es el argumento, x + 1 es el return, increment_v2 es la variable que guardara la funcion
increment_v2 = lambda x : x + 1 

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('Eduardo', 'Solorio Hernández')
print(text)