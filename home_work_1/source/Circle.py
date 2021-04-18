from home_work_1.source.Figure import Figure
from home_work_1.source.Triangle import Triangle
from math import pi


class Circle(Figure):
    def __init__(self, name, angles, radius):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.radius = radius

    def get_circle_area(self):
        """Площадь окружности"""
        return 2 * pi * self.radius ** 2

    def get_circle_length(self):
        """Длина окружности"""
        return 2 * pi * self.radius

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            return Circle.get_circle_area(self) + Triangle.get_triangle_area(figure)
        else:
            return print('Передан неправильный класс')
