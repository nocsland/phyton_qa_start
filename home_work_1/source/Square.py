from Figure import Figure


class Square(Figure):
    def __init__(self, name, angles, side):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.side = side

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(Square, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта rectangle
square = Square(name='square', angles=4, side=6)

# Площадь прямоугольника
square.area = square.side ** 2

# Периметр прямоугольника
square.perimeter = 4 * square.side
