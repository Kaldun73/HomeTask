#7. Необходимо создать (не программно) текстовый файл, где каждая
# строка описывает учебный предмет и наличие лекционных, практических
# и лабораторных занятий по этому предмету и их количество. Важно,
# чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.


with open("text6.txt") as my_f:
    lesson_dict = {}
    hours = []
    for subject in my_f:
        subject_split = subject.split()
        subject_name = subject_split[0]
        all_hours = subject_split[1:]
        lesson_dict[subject_name] = 0
        for types in all_hours:
            try:
                lesson_dict[subject_name] += int(types[:types.find("(")])
            except ValueError:
                pass
print(lesson_dict)

my_f.close()