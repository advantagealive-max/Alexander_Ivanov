# 14. Создайте функцию merge_dicts(*dicts), которая объединяет несколько словарей в один.
# При совпадении ключей используется последнее значение.
# Пример вызова:
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# d3 = {"c": 5, "d": 6}
# print(merge_dicts(d1, d2, d3))
# Ожидаемый результат:
# {'a': 1, 'b': 3, 'c': 5, 'd': 6}
# """


def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))