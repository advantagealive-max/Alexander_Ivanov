# 2. Напишите функцию counter(start=0), которая возвращает вложенную функцию.
# Каждый вызов вложенной функции должен увеличивать счетчик на 1.
# Пример вызова:
#
# c1 = counter(5)
# c2 = counter()
#
# print(c1())  # 6
# print(c1())  # 7
# print(c2())  # 1
# print(c2())  # 2
#
# Подсказка: используйте nonlocal
# """

def counter(start=0):
    count = start
    def count_pl():
        nonlocal count
        count += 1
        return count
    return count_pl

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2
