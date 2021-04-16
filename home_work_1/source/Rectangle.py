from home_work_1.source.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, angles, length, width):
        """Конструктор класса"""
        self.name = name
        self.angles = angles
        self.length = length
        self.width = width

    def get_rectangle_area(self):
        """Площадь прямоугольника"""
        rectangle_area = self.length * self.width
        return rectangle_area

    def get_rectangle_perimeter(self):
        """Периметр прямоугольника"""
        rectangle_perimeter = 2 * (self.length + self.width)
        return rectangle_perimeter

    def add_area_rectangle(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта rectangle
rectangle = Rectangle(name='rectangle', angles=4, length=5, width=7)

# Инициализация и передача из данных из функции для rectangle.area
rectangle.area = Rectangle.get_rectangle_area(rectangle)

# Инициализация и передача из данных из функции для rectangle.perimeter
rectangle.perimeter = Rectangle.get_rectangle_perimeter(rectangle)
