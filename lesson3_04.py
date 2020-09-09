# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    result1 = x ** y
    result2 = 1
    while y < 0:
        result2 = result2 * x
        y += 1
        result2 = 1 / result2
        return result1, result2

try:
    x_num = int(input('Укажите действительное положительное число x: '))
    while x_num <= 0:
        x_num = int(input('Неправильное значение! Укажите действительное положительное число x: '))
    y_num = int(input('Укажите целое отрицательное число y: '))
    while y_num >= 0:
        y_num = int(input('Неправильное значение! Укажите целое отрицательное число y: '))
    result_1, result_2 = my_func(x=x_num, y=y_num)
    print(f'Результат возведения х в степень у (1-й способ): {result_1}')
    print(f'Результат возведения х в степень у (2-й способ): {result_2}')
except ValueError:
    print('Ошибка')
