# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


my_dict = {}
with open('test_6.txt') as f_o:
    for line in f_o:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or i.isdigit()]).split()))
        my_dict[name] = name_sum
print(my_dict)

# ошибка, если список в текстовом файле на русском языке.
my_dict = {}
with open('test_6_1.txt') as f_o:
    for line in f_o:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or i.isdigit()]).split()))
        my_dict[name] = name_sum
print(my_dict)


# Я так поняла из гугла, что нужно сделать импорт кодировки, попробовала несколько кодов, но не получилось.
# Traceback (most recent call last):
#   File "C:/Users/Home/PycharmProjects/Python_basic/lesson5_06.py", line 22, in <module>
#     for line in f_o:
#   File "C:\Users\Home\AppData\Local\Programs\Python\Python38-32\lib\encodings\cp1251.py", line 23, in decode
#     return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>
