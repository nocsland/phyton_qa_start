from Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, angles, length, width):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.length = length
        self.width = width

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(Rectangle, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта rectangle
rectangle = Rectangle(name='rectangle', angles=4, length=5, width=7)

# Площадь прямоугольника
rectangle.area = rectangle.length * rectangle.width

# Периметр прямоугольника
rectangle.perimeter = 2 * (rectangle.length + rectangle.width)
