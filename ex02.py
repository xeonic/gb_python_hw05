# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_f = open('ex02.txt', 'r', encoding='utf8')
i = 0
for line in my_f:
    print(f'{line}\nwords count:{len(line.split())}')
    i += 1
my_f.close()
print(f'lines count: {i}')

