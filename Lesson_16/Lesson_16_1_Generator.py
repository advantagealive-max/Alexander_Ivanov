# gen = (x ** 3 for x in range(11))
# # print(gen)
# print(type(gen))
# #
# for x in gen:
#     print(x)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# # print(sum(gen))
# print(list(gen))
#
def counter():
    x = 1
    while True:
        yield x
        x += 1

counter_0 = counter()
print(next(counter_0))
print(next(counter_0))
print(next(counter_0))
print(next(counter_0))
print(next(counter_0))
print(next(counter_0))
print(next(counter_0))



