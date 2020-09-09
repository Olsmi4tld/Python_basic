# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input('enter your name: ')
surname = input('enter your surname: ')
year = int(input('enter your year of birth: '))
city = input('enter city: ')
email = input('enter e-mail: ')
tel = input('enter telephone number: ')

def my_func(name, surname, year, city, email, tel):
    return ' '.join([name, surname, str(year), city, email, tel])
print(my_func(name, surname, year, city, email, tel))
