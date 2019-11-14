#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться
# на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("text4.txt", 'r') as my_f:
    content = my_f.readlines()
    new_list = []
    for i in range(0, len(content)):
        number = content[i].split(' - ')
        if number[0] == 'One':
            new_list.append(f"Один - {i + 1}")
        elif number[0] == 'Two':
            new_list.append(f"Два - {i + 1}")
        elif number[0] == 'Three':
            new_list.append(f"Три - {i + 1}")
        elif number[0] == 'Four':
            new_list.append(f"Четыре - {i + 1}")
    print(new_list)

    with open("text4.1.txt", 'w') as f:
        for item in new_list:
            f.write("%s\n" % item)

my_f.close()