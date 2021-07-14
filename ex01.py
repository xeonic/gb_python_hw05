# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

str_list = []
while True:
    input_str = input('Input string (for end press enter) - ')
    if input_str == '':
        break
    else:
        str_list.append(input_str + '\n')

out_f = open("ex01.txt", "w")
out_f.writelines(str_list)
out_f.close()
