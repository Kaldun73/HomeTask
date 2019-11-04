#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.


number = int(input("Введите целое положительное число"))

if number < 0:
    number = int(input("Вы ввели отрицательное число. Введите целое положительное число"))

if number > 0:
    list = []
    while number > 10:
        list.append(number % 10)
        number //= 10
    result = max(list)
    print(result)


