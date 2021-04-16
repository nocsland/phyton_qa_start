from home_work_1.source.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, name, angles, radius):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.radius = radius

    def get_circle_area(self):
        circle_area = 2 * pi * self.radius ** 2
        return circle_area

    def get_circle_length(self):
        circle_length = 2 * pi * self.radius
        return circle_length

    def add_area_circle(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта circle
circle = Circle(name='circle', angles=0, radius=6)

# Инициализация circle.area
circle.area = Circle.get_circle_area(circle)

# Инициализация circle.length
circle.length = Circle.get_circle_length(circle)
