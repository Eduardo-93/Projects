#IMPORTANTE, el usar r+ da permisos de escritura y de lectura, en este caso modifica el archivo mas no lo sobreescribe como es el caso de w+
#w+ Da tambien permisos de lectura y escritura pero este sobreescribe todo el archivo, lo que significa que borra todo y lo cambia por lo nuevo 
# si solo se usa w borra todo el archivo. CUIDADO!!!!!
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNuevas cosas en este archivo\n')
    file.write('Otra linea\n')
    file.write('una mas\n')