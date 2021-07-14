# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

rus_dict = {1: 'Odin', 2: 'Dva', 3: 'Tri', 4: 'Chetyre'}
out_list = []
in_f = open("ex04_in.txt", "r", encoding='utf8')
out_f = open("ex04_out.txt", "w", encoding='utf8')
for line in in_f:
    try:
        in_str_list = line.split(sep=' — ')
        out_f.writelines(f'{int(in_str_list[1])} — {rus_dict.get(int(in_str_list[1]))}\n')
    except ValueError:
        print('Wrong input string')
in_f.close()
out_f.close()
