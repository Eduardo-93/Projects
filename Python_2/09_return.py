def find_volume(length = 1, width = 1, depth = 1): #si no se dan valores tomara los de 1
    return length * width * depth, width, 'hola'

result = find_volume(10, 5, 40)
print("Valores en todo", result)

result_2 = find_volume()
print("Sin valores", result_2)

result_3 = find_volume(depth = 10)
print("Solo depth", result_3)

print("*" * 10)

result, width, text = find_volume(length = 5, width = 10)
print(result)
print(width)
print(text)