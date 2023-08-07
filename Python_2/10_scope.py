price = 100 #Contexto Global

def increment():
    price = 200 #Contexto Local
    result = price + 10
    print(result)
    return result


print(price)
price_2 = increment()
print(price_2)
# print(result) -> Da error porque result es un scope local, por lo que solo se encuentra dentro de la funcion increment