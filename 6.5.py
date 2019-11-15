#Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут t itle
#(название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
#три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
#реализовать переопределение метода draw. Для каждого из классов методы должен
#выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
#описанный метод для каждого экземпляра.

class Stationery:
    def draw(self, title):
        title = "title"
        print(f"Запуск отрисовки {title}")

class Pen(Stationery):
    def draw(self, title):
        print(f"Запуск отрисовки ручкой {title}")

class Pencil(Stationery):
    def draw(self, title):
        print(f"Запуск отрисовки карандашом {title}")

class Handle(Stationery):
    def draw(self, title):
        print(f"Запуск отрисовки маркером {title}")

pen = Pen()
pen.draw("ручка")
pencil = Pencil()
pen.draw("карандаш")
handle = Handle()
pen.draw("маркер")