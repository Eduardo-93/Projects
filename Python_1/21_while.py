#sintaxis
'''
counter = 0

while counter < 10:
    counter += 1
    print(counter)
'''
'''
counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break # Rompe el ciclo
    print(counter)
'''

counter = 0

while counter < 20:
    counter += 1
    if counter < 15: # Si counter es menor a 15 aplica el continue y continua el ciclo sin ejecutar el print
        continue #brinca al inicio del ciclo sin tomar el cuenta lo que esta abajo del ciclo
    print(counter) # Solo imprimira los numeros menores a 15