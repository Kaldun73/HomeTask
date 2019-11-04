#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds_time = int(input("Введите время в секундах"))
print(f'Время {seconds_time} секунд')
hours = seconds_time // 3600
minutes = int((seconds_time % 3600) / 60)
seconds = int((seconds_time % 3600) % 60)
print(f'Время {seconds_time} секунд составляет {hours}:{minutes}:{seconds}')