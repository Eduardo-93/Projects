def increment(x):
    return x + 1

def high_order_function(x, func):
    return x + func(x)

result = high_order_function(2, increment)

#seria el resultaod de la high order function 2 + (2 + 1)
print(result)

#con lambda

increment_v2 = lambda x: x + 1
high_order_function_v2 = lambda x, func: x + func(x)
result_v2 = high_order_function_v2(2, increment_v2) # Con lambda es posible escribir solo la funcion sin necesidad de definir una anteriormente:
result_v2 = high_order_function_v2(2, lambda x: x * 5) # De esta forma
print(result_v2)