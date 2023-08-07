text = "Ella sabe Python"
print('size =',len(text)) #numero de caracteres en el texto
print(text[0]) #posicion inicial 0
print(text[15]) #posicion final size - 1
print(text[-1]) #Posicion final -1
print(text[-16]) #Posicion inicial size * -1
print(text[0:5]) #Lo que esta dentro de la posicion 0 a la 5

#Slicing
print(text[10:16])
print(text[0:10]) #Inicia de la posicion cero
print(text[:10]) #Es lo mismo que de 0:10
print(text[5:-1])
print(text[5:]) #De inicio a final
print(text[:]) #De inicio al final
print(text[10:16:1]) #Va del caracter 10 al 16 en saltos de 1
print(text[10:16:2]) #Va del caracter 10 al 16 en saltos de 2
print(text[::2]) #Va de inicio a final en saltos de dos caracteres