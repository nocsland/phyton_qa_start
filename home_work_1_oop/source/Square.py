from home_work_1.source.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, angles, length, width):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.length = length
        self.width = width
        self.area = self.get_area()

