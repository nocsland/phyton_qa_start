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

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            from home_work_1.source.Circle import Circle
            return Square.get_square_area(self) + Circle.get_circle_area(figure)
        else:
            return print('Передан неправильный класс')
