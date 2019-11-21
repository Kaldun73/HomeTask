'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def calculate(self):
        return f"Textile amount for coat {self.param/6.5 + 0.5}"

class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def calculate(self):
        return f"Textile amount for coat {2*self.param + 0.3}"

coat = Coat(13)
print(f"Textile amount for coat {coat.calculate}")

suit = Suit(160)
print(f"Textile amount for coat {suit.calculate}")
