#6. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

total = 0
with open("text5.txt", 'w') as my_f:
    for i in range(100):
        number = randint(1, 100)
        total += number
        my_f.write(str(number) + ' ')

print(f"Сумма элементов - {total}")


my_f.close()