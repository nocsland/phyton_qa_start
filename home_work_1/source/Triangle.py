from home_work_1.source.Figure import Figure
from home_work_1.source.Rectangle import Rectangle


class Triangle(Figure):
    """Конструктор треугольника"""
    def __init__(self, name, angles, base, height, side_a, side_b, side_c):
        self.name = name
        self.angles = angles
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_triangle_area(self):
        """Площадь треугольника"""
        return 0.5 * self.base * self.height

    def get_triangle_per(self):
        """Периметр треугольника"""
        return self.side_a + self.side_b + self.side_c

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            return Triangle.get_triangle_area(self) + Rectangle.get_rectangle_area(figure)
        else:
            return print('Передан неправильный класс')

