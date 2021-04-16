from home_work_1.source.Figure import Figure


class Square(Figure):
    def __init__(self, name, angles, side):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.side = side

    def get_square_area(self):
        """Площадь квадрата"""
        square_area = self.side ** 2
        return square_area

    def get_square_perimeter(self):
        """Периметр квадрата"""
        square_perimeter = 4 * self.side
        return square_perimeter

    def add_area_square(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта rectangle
square = Square(name='square', angles=4, side=6)

# Инициализация и передача из данных из функции для square.area
square.area = Square.get_square_area(square)

# Инициализация и передача из данных из функции для square.perimeter
square.perimeter = Square.get_square_perimeter(square)
