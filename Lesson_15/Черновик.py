# Получение даты и времени для логирования:
# import datetime
# print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
#
# Пример содержимого файла после нескольких запусков:
#
# 2024-02-16 14:30:01 Запуск программы
# 2024-02-16 14:35:15 Запуск программы
# 2024-02-16 14:40:22 Запуск программы
# """


import datetime

data_file = 'log.txt'

with open(data_file, 'a+', encoding='utf-8') as f:
    f.read()
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S Запуск программы'))
    f.write('\n')
