from home_work_1.source.Figure import Figure
from home_work_1.source.Square import Square


class Rectangle(Figure):
    def __init__(self, name, angles, length, width):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.length = length
        self.width = width

    def get_rectangle_area(self):
        """Площадь прямоугольника"""
        return self.length * self.width

    def get_rectangle_perimeter(self):
        """Периметр прямоугольника"""
        return 2 * (self.length + self.width)

    def add_area(self, figure):
        """Объект элемент класса"""
        if isinstance(figure, Figure):
            return Rectangle.get_rectangle_area(self) + Square.get_square_area(figure)
        else:
            return print('Передан неправильный класс')
