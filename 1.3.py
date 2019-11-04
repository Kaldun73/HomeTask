#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = str(input("Введите число от 1 до 9"))
number2 = (number + number)
number3 = (number2 + number)
number = int(number)
number2 = int(number2)
number3 = int(number3)
result = number + number2 + number3
print(result)