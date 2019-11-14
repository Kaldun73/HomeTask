#Реализовать класс Road (дорога), в котором определить атрибуты: length(длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты
# сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def built(self):
        while True:
            amount = 0
            try:
                self._lenght = int(input("Input lenght of the road: "))
                self._width = int(input("Input width of the road: "))
                self.height = int(input("Input height of the road: "))
                amount = self._lenght * self._width * 0.025 * self.height
                print(f'Для постройки дороги толщиной {self.height} см потребуется {amount} тонн асфальта')
                break
            except ValueError:
                print("Input correct value")

asphalt = Road()
asphalt.built()