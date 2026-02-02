# 5. Проверка, является ли объект итерируемым
# Создайте список внутри которого 3 объекта: число, строка и список.
# Создайте генератор в котором будет написано True - если объект является итерируемым или False - если нет

#
# list_x = [4, 'stroka', [True, 'str_in']]
# result  = [True if not st.isdigit() else False for st in list_x]
#
# print(list_x)


# N = int(input('Введите число: '))
# i = 2
# res = False
# while i < N:
#     if N % i == 0:
#         res = True
#         break
#     else:
#         i += 1
# print('Простое число' if res == False else 'Не простое число' )


num = input('Введите число(0 для выхода из программы): ')
max_num = 0
if num.isdigit():
    while int(num) != 0:
        if int(num) > max_num:
            max_num = int(num)
        num = input('Введите число(0 для выхода из программы): ')
        if not num.isdigit():
            print('Программа остановлена (не верные данные ввода')
            break
    else:
        print('Программа остановлена (введен 0)')
    print(max_num)

else:
    print('Программа остановлена (не верные данные ввода)')

