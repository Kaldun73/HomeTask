#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

distance = int(input("Введите дистанцию, которую спортсмен пробежал в первый день"))
target = int(input("Введите дистанцию, которой он должен достигнуть"))
i = 1
while distance <= target:
    distance = distance * 1.1
    i += 1
print(f'Спортсмен превысит дистанцию {target} км через {i} дней после начала тренировки')
