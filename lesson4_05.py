# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def nul_list(el_1, el_2):
    return el_1 * el_2

unique_list = [el for el in range(100, 1001, 2)]
print(f'List\n{unique_list}\nMultiplication of numbers\n{reduce(nul_list, unique_list)}')