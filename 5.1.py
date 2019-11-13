#1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка.

while True:
    text = input(("Введите данные. Для выхода нажмите Enter") + "\n").split()
    if not text:
        break
    with open("text1.txt", "a") as f:
        for i in range(len(text)):
            print(text[i], file=f)

f.close()