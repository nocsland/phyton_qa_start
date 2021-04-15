from Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, name, angles, radius):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.radius = radius

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(Circle, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта circle
circle = Circle(name='circle', angles=0, radius=6)

# Площадь круга
circle.area = 2 * pi * circle.radius ** 2

# Длина окружности
circle.perimeter = 2 * pi * circle.radius
