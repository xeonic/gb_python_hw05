# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("ex05.py.txt", "w") as f_obj:
    for _ in range(0, 10):
        f_obj.writelines(f'{randint(0, 10)} ')
with open("ex05.py.txt", "r") as f_obj:
    print(f'elements sum: {sum(map(int, f_obj.readline().split()))}')
