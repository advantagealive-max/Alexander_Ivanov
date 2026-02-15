# 1. Оставь только строки и списки из списка:
# items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
# Ожидаемый результат:
# ['hello', [1, 2], 'world']

# items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
# items_true = list(filter(lambda item: isinstance(item, (list, str)), items))

# 2. Создай функцию describe_type(x), которая:
# печатает "Это строка", если x — строка
# "Это число", если x — int или float
# "Это булевое значение", если x — bool
# "Неизвестный тип" — в остальных случаях
# Пример вызова:
# describe_type(5.5)       # Это число
# describe_type(True)      # Это булево значение
# describe_type("Привет")  # Это строка
# describe_type([1, 2, 3]) # Неизвестный тип


# def describe_type(x):
#     if isinstance(x, bool):
#         print('Это булевое значение')
#     elif isinstance(x, str):
#         print('Это строка')
#     elif isinstance(x, (int, float)):
#         print('Это число')
#     else:
#         print('неизвестный тип')
#
# describe_type(5.5)       # Это число
# describe_type(True)      # Это булево значение
# describe_type("Привет")  # Это строка
# describe_type([1, 2, 3]) # Неизвестный тип

# 3. Создай функцию filter_list(f, data: list[int]) -> list[int],
# которая возвращает только те элементы из data, которые проходят проверку функцией f.
# Проверь на функции lambda x: x > 3 и списке [1, 3, 5, 7].
#
#
# def filter_list(f, data: list[int]) -> list[int]:
#     return [x for x in data if f(x)]
# print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))

# 5. Создай функцию def analyze(data),
# которая выводит количество элементов и среднее значение, если список не пустой.

# def analyze(data):
#     if data:
#         count = len(data)
#         average = sum(data) / count
#         print(f'Количество элементов: {count}')
#         print(f'Среднее значение: {average}')
# analyze([10, 20, 30, 40, 50])

# 6. Список логических значений:
# flags = [True, True, True, False]
# Проверь:
# Все ли значения истинные
# Есть ли среди них хотя бы одно истинное
# Ожидаемый результат:
# False
# True

# flags = [True, True, True, False]
# print(all(flags))
# print(any(flags))