# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('test.txt', 'r') as f_o:
    lines = f_o.readlines()
    print(f"Всего строк: {len(lines)}")
    for line in lines:
        print(f"{line[:-1]} {len(line)}")


