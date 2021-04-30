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
        self.area = self.get_area()

    def get_area(self):
        """Площадь треугольника"""
        return 0.5 * self.base * self.height

    def get_perimeter(self):
        """Периметр треугольника"""
        return self.side_a + self.side_b + self.side_c
