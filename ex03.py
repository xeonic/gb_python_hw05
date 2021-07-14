# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import json

employees = []

out_f = open("ex03.txt", "w")
while True:
    input_emp = input('Input surname (for end press enter) - ')
    if input_emp == '':
        break
    else:
        new_item = {'surname': input_emp,
                    'salary': int(input('Input salary - '))}
        employees.append(new_item)

out_f.writelines(json.dumps(employees))
out_f.close()

salary_sum = []
for emp in employees:
    salary_sum.append(emp.get('salary'))
    if emp.get('salary') > 20:
        print(f"{emp.get('surname')} has salary {emp.get('salary')}")
try:
    print (f'average salary: {sum(salary_sum) / len(salary_sum)}')
except ZeroDivisionError:
    print ('Empty employee list')
