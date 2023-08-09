lista = []
for i in range(1, 11):
    lista.append(i)
print(lista, '\n')

lista_v2 = [i for i in range(1, 11)]
print(lista_v2)

# Forma "manual" de hacer un for, asi funciona
my_iter = iter(range(1, 11))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))