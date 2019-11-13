#2. Создать текстовый файл (не программно), сохранить в нем
# несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open("text2.txt", 'r') as my_f:
    content = my_f.readlines()
    lines = len(content)
    print(f'Количество строк в файле: {lines}')
    for i in range(0, len(content)):
        print(f'Количество слов в строке {i+1}: {len(content[i].split())}')

my_f.close()