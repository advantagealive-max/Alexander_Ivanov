

# Создай список cities с элементами: "Москва", "Тверь", "Вологда".
cities = ["Москва", "Тверь", "Вологда"]
print(cities)

# Создай список numbers с целыми числами от 1 до 5.
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Создай список mixed с элементами разных типов: число, строка, булево значение, вещественное число.
mixed = [1, 'Stroka', True, 3.4]
print(mixed)
# Выведи первый элемент списка cities.
print(cities[0])

# Выведи последний элемент списка numbers с помощью отрицательного индекса.
print(numbers[-1])

# Попробуй получить элемент с индексом 10 из cities. Что произойдет?
# print(cities[10]) # list index out of range

# Замени второй элемент списка numbers на 10.
numbers[1] = 10
print(numbers)

# Замени последний элемент списка mixed на "Python".
mixed[-1] = 'Python'
print(mixed)

# Выведи длину списка numbers.
print(len(numbers))

# Найди максимальное и минимальное значение в numbers.
print(max(numbers))
print(min(numbers))

# Вычисли сумму всех элементов списка numbers.
print(sum(numbers))

# Отсортируй список numbers по возрастанию и убыванию.
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# Объедини два списка [1, 2, 3] и [4, 5].
first_str = [1, 2, 3]
second_str = [4, 5]
print(first_str + second_str)

# Продублируй список ["Python", "is", "awesome"] три раза.
list_python = ['Python', 'is', 'awesome']
print(list_python * 3)

# Проверь, содержится ли число 3 в списке numbers.
print(3 in numbers)

# Проверь, содержится ли "Москва" в cities.
print('Москва' in cities)

# Проверь, содержится ли [1, 2] в mixed.
print([1, 2] in mixed)

# Удали третий элемент из numbers.
print(numbers)
del numbers[2]
print(numbers)

# Удали последний элемент из cities с помощью del.
del cities[-1]
print(cities)

# Преобразуй строку "Python" в список символов.
list1 = list('Python')
print(list1)

# Найди максимальный и минимальный символ в этом списке.
print(max(list1))
print(min(list1))
print(ord(list1[0]), ord(list1[1]), ord(list1[2]), ord(list1[3]), ord(list1[4]), ord(list1[5])) # чтобы убедиться

# Попробуй сложить все элементы списка. Что произойдет?
# print(sum(list1)) складвать строки нельзя

# Создай список с городами.
cities = ["Санкт-Петербург", "Самара", "Калиниград", "Саратов"]

# Создай копию списка с помощью среза.
cities_copy = cities[::]
print(cities_copy)

# Проверь, является ли оригинальный список и его копия разными объектами.
print(id(cities_copy), id(cities))

# Выведи 2-й и 3-й элементы списка с городами.
print(cities[1:3])

# Выведи все элементы, начиная с 3-го.
print(cities[2:])

# Выведи первые три элемента.
print(cities[:3])

# Выведи весь список через срез.
print(cities[:])

# Используй отрицательные индексы для выбора последних двух элементов.
print(cities[-2:])

# Выведи каждый второй элемент списка с городам.
print(cities[1::2])

# Выведи список в обратном порядке.
print(cities[::-1])

# Выведи каждый второй элемент с конца.
print(cities[::-2])

# Замени 2-й и 3-й элементы списка с городами на "Сочи" и "Нижний Новгород".
cities[1] = 'Сочи'
cities[2] = 'Нижний Новгород'
print(cities)

# Замени каждый второй элемент на "Город".
cities [1::2] = ['Город'] * len(cities[1::2])
print(cities)

# Присвой новые значения кортежем: cities[1:3] = "Волгоград", "Омск".
cities[1:3] = ("Волгоград", "Омск")
print(cities)

# Объедини два списка [1, 2, 3] и [4, 5, 6].
num_3 = [1, 2, 3] + [4, 5, 6]
print(num_3)

# Продублируй список ["Python", "rocks"] два раза.
list_3 = ['Python', 'rocks']
print(list_3 * 2)

# Сравни [1, 2, 3] и [1, 2, 3] – равны ли они?
print([1, 2, 3] == [1, 2, 3])

# Проверь, что [10, 5, 3] > [5, 10, 3].
print([10, 5, 3] > [5, 10, 3])

# Попробуй сравнить [1, 2, 3] и [1, 2, "abc"]. Что произойдет?
# print([1, 2, 3] > [1, 2, "abc"]) # ошибка

# Создай список chars = list("Python").
chars = list('Python')
print(chars)

# Выведи максимальный и минимальный символ в этом списке.
print(max(chars))
print(min(chars))

# Попробуй сложить все элементы списка chars. Объясни результат.
# print(sum(chars)) # нельзя сложить строки.

# Создай список numbers = [5, 10, 15].
numbers = [5, 10, 15]

# Добавь в конец списка число 20 с помощью append().
numbers.append(20)
print(numbers)

# Вставь число 7 на второе место списка с помощью insert().
numbers.insert(1, 7)
print( numbers)

# Добавь строку "Python" в список numbers.
numbers.append('Python')
print(numbers)

# Удали число 10 из списка с помощью remove().
numbers.remove(10)
print(numbers)

# Удали последний элемент списка и выведи его (pop()).
print(numbers.pop())


# Удали элемент с индексом 1 с помощью pop().
numbers.pop(1)
print(numbers)

# Очисти весь список numbers.
numbers.clear()
print(numbers)

# Создай список letters = ["a", "b", "c"].
letters = ['a', 'b', 'c']

# Создай копию списка с помощью copy() и list().
letters2 = letters.copy()
letters3 = list(letters)
print(letters2)
print(letters3)

# Проверь, являются ли оригинальный список и копия разными объектами.
print(id(letters), id(letters2), id(letters3))

# Создай список marks = [2, 3, 5, 3, 4, 5, 2, 3].
marks = [2, 3, 5, 3, 4, 5, 2, 3]

# Определи, сколько раз встречается число 3 в списке (count()).
print(marks.count(3))

# Найди индекс первого вхождения числа 5 (index()).
print(marks.index(5))

# Проверь, содержится ли число 6 в списке перед вызовом index().
print(6 in marks)
# print(marks.index(6))

# Создай список nums = [8, 2, 5, 1, 7].
nums = [8, 2, 5, 1, 7]

# Отсортируй его по возрастанию (sort()).
nums.sort()
print(nums)
# Отсортируй его по убыванию (sort(reverse=True)).
nums.sort(reverse=True)
print(nums)

# Разверни список (reverse()).
nums.reverse()
print(nums)

# Создай список cities.
cities = ["Moscow", "Saint_Peterburg", "Saratov", "Samara", "Astrahan"]

# Отсортируй его в алфавитном порядке (sort()).
# cities.sort()
# print(cities)

# Создай новый отсортированный список с sorted(), не изменяя оригинал.
cities_new = sorted(cities)
print(cities_new)

# Создай список символов chars = list("programming").
chars = list('programming')

# Определи количество вхождений буквы "g".
print(chars.count('g'))


# Разверни список символов (reverse()).
chars.reverse()
print(chars)

# Попробуй отсортировать список chars (sort()). Как изменится порядок букв?
chars.sort()
print(chars)

# Создай двумерный список matrix, содержащий 3 строки и 4 столбца со значениями от 1 до 12.
matrix_2d = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]


# Выведи всю матрицу на экран.
print(matrix_2d)

# Выведи вторую строку.
print(matrix_2d[1])

# Выведи первый элемент третьей строки.
print(matrix_2d[2][0])

# Замени все элементы первой строки на 0.
matrix_2d[0] = [0, 0, 0, 0]
print(matrix_2d)

# Замени последний элемент второй строки на "Python".
matrix_2d[1][-1] = 'Python'
print(matrix_2d)