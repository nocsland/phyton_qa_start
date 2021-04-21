from home_work_1.source.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, name, angles, radius):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.radius = radius
        self.area = self.get_area()

    def get_area(self):
        """Площадь окружности"""
        return 2 * pi * self.radius ** 2

    def get_perimeter(self):
        """Длина окружности"""
        return 2 * pi * self.radius

