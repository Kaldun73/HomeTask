#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
#строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
#среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
#также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
#словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
#Подсказка: использовать менеджер контекста.

import json

with open("text7.txt", 'r') as my_f:
    for i in range(3):
        text = my_f.write(input("Введите данные через пробел: Название фирмы, форма собственности, выручка, издержки") + "\n")
    content = my_f.readlines()
    print(content)
    result_dict = {}
    profit = {}
    for i in range(0, len(content)):
        firm_i = content[i].split(' ')
        name = firm_i[1] + " " + firm_i[0]
        result = int(firm_i[2]) - int(firm_i[3])
        result_dict.update({name: result})
    av_profit = round(sum(result_dict.values()) / len(content), 2)
    profit.update({'average_profit': av_profit})

    listed = [result_dict, profit]
    print(listed)

with open("5.7.json", "w", encoding="utf-8") as my_f:
    json.dump(listed, my_f, ensure_ascii=False)

