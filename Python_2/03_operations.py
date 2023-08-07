set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b) #Concatena los conjuntos a y b, no agrega los repetidos
print(set_c)
print(set_a | set_b) #el operador | es la suma de dos conjuntos, da el mismo resultado de union pero en este caso solo se imprime

set_c = set_a.intersection(set_b) #Une los conjuntos a y b pero solo guarda los elementos repetidos
print(set_c)
print(set_a & set_b) #& funciona igual que intersection

set_c = set_a.difference(set_b) #Resta set_a - set_b, solo dara el resultado de set_a menos los elementos repetidos con set_b
print(set_c)
print(set_a - set_b)

set_c = set_a.symmetric_difference(set_b) # Hace una union de set_a con set_b sin agregar los elementos iguales de ambos conjuntos. En este caso bol se queda fuera ya que se repetiria al momento de hacer la union
print(set_c)
print(set_a ^ set_b)