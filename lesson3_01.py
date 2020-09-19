# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(s1, s2):
    try:
        s1, s2 = int(s1), int(s2)
        div_num = s1 / s2
        return round(div_num, 4)
    except ValueError:
        return "Value error!"
    except ZeroDivisionError:
        return "Error! Zero division."
print(division(int(input("Enter number 1 = ")), int(input("Enter number 2 = "))))
