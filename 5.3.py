#3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

with open("text3.txt", 'r') as my_f:
    content = my_f.readlines()
    wage = []
    low_wage_list = []
    for i in range(0, len(content)):
        person = content[i].split(': ')
        wage.append(int(person[1]))
        if int(person[1]) < 20000:
            low_wage_list.append(person[0])
    print(f'Список людей, получающих менее 20000 рублей: {low_wage_list}')
    average = sum(wage) / len(content)
    print(f'Средняя зарплата всех сотрудников: {average} рублей')

my_f.close()