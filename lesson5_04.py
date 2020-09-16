# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num_dict = {'One': 'Один',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре'}
with open('test_2.txt', 'r') as f_o:
    with open('test_3.txt', 'w') as final_file:
        lines = f_o.readlines()
        for line in lines:
            num_list = line.split(" - ")
            final_file.write(f'{num_dict[num_list[0]]} - {num_list[1]}')


#ошибка -
# C:\Users\Home\PycharmProjects\Python_basic\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/Python_basic/lesson5_04.py
# Traceback (most recent call last):
#   File "C:/Users/Home/PycharmProjects/Python_basic/lesson5_04.py", line 19, in <module>
#     final_file.write(f'{num_dict[num_list[0]]} - {num_list[1]}')
# KeyError: 'One вЂ” 1\n'



