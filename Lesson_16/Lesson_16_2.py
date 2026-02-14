# cities = ['Moscow', 'Samara', 'Togliatty']
# reverse = map(lambda str_1: str_1[::-1], cities)
# print(list(reverse))
a = [index for index in range(10)]
b = (index for index in range(10))
c = {index for index in range(10)}

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
