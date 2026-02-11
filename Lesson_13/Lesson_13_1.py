def decor(func):
    def wrapper(*args, **kwargs):
        print('до выполнения функции')
        print('args: ', *args)
        print('kwargs', kwargs)
        return func(*args, **kwargs)
        func(*args, **kwargs)
        print('после выполнения функции')
    return wrapper

@decor
def print_text(text):
    print(f'Простой текст {'дополнительный текст'}')

print_text(text='Дополнительный текст')
#
import time

def count_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения: {end_time - start_time} сек')
        return result
    return wrapper

@count_timer
def func_1(*args, **kwargs):
    time.sleep(3)
    print('Функция отработала')
    return 'Воврат из функции'

res = func_1()
print(res)

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Функция: {func.__name__}\nНеименованные аргументы: {args}\nИменнованные аргументы: {kwargs}\n ')
        result = func(*args, **kwargs)
        print(f'Результат функции: {result}')
        return result
    return wrapper


@count_timer
@logger
def summer(first, second):
    return first + second

result = summer(1,second= 2)