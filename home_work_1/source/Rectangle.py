from home_work_1.source.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, angles, length, width):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.length = length
        self.width = width
        self.area = self.get_area()

    def get_area(self):
        """Площадь прямоугольника"""
        return self.length * self.width

    def get_perimeter(self):
        """Периметр прямоугольника"""
        return 2 * (self.length + self.width)
