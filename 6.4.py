#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
#color, name, is_police ( булево). А также методы: go, stop, t urn(direction), которые должны
#сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
#дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
#show_speed, который должен показывать текущую скорость автомобиля. Для классов
#TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
#( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
#атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool

    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn_left(self):
        print("Машина повернула налево")
    def turn_right(self):
        print("Машина повернула направо")
    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def Town(self):
        if self.speed > 60:
            print("Вы превысили скорость")


towncar = TownCar(70, "grey", "Corolla", False)
towncar.Town()
towncar.stop()
towncar.turn_left()
towncar.go()

class SportCar(Car):
    def Sport(self):
        self.speed = 300

sportcar = SportCar(200, "red", "Acura", False)
sportcar.show_speed()

class WorkCar(Car):
    def Work(self):
        if self.speed > 40:
            print("Вы превысили скорость")

workcar = WorkCar(30, "black", "Renault", False)
workcar.Work()

class PoliceCar(Car):
    def Police(self):
        if True:
            print("Машина является полицейской")

policecar = PoliceCar(70, "blue", "Lada", True)
policecar.Police()