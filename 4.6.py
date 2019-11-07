# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from sys import argv
from itertools import count
from itertools import cycle


for el in count(28390):
    print(el)

i = 0
for el in cycle("abcdefghijklmopqrstuvwxyz"):
    print(el)
    i += 1
