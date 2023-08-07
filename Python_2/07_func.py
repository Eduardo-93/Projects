print('Esto es una funcion')

def my_print(text):
    print('This is my print')
    print(text * 2)
    print('This is my print 2')

my_print('Este es mi texto. ')

my_print('Hola, segunda llamada funcion. ')

a = 10
b = 90

c = a + b

def suma(a, b):
    print(a + b) #Imprime solo la suma
    my_print(a + b) #Imprime todo por 2 porque en la funcion my_print toma el text y lo multiplica por 2

suma(1, 5) #6
suma(10, 4) #14