#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str('\n'.join('\t'.join([str(j) for j in i]) for i in self.args))

    def __add__(self, other):
        self.other = Matrix(other)
        result = []
        numbers = []
        if len(other.args) == len(self.args):
            for i in range(len(self.args)):
                for j in range(len(self.args[i])):
                    numbers.append(self.args[i][j] + other.args[i][j])
                    if len(numbers) == len(self.args[i]):
                        result.append(numbers)
                        numbers = []
        else:
            print("Размерности не совпадают")
        return result

m_new_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_new_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(m_new_1)
print(m_new_1 + m_new_2)

