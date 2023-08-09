file = open('./text.txt')
#print(file.read()) # Toma todo el texto y lo imprime

'''
#Lee linea a linea, si hay varios, cada uno representa un renglon
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''
# Es lo mismo que el anterior pero en este caso no almacena tanta memoria como si abriera por completo el archivo
for line in file:
    print(line)

#IMPORTANTE. De esta forma se cierra el archivo lo cual libera memoria. Es importante saber cuando cerrar el archivo
file.close()

#Al hacer esto no es necesario cerrar el archivo ya que lo cierra de forma automatica
with open('./text.txt') as file:
    for line in file:
        print(line)