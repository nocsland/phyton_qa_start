from Figure import Figure


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

    @staticmethod
    def get_triangle_area(base, height):
        """Площадь треугольника"""
        tr_area = 0.5 * base * height
        return tr_area

    @staticmethod
    def get_triangle_per(a, b, c):
        """Периметр треугольника"""
        tr_per = a + b + c
        return tr_per

    @staticmethod
    def add_area(figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            total_area = figure.area + triangle.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта triangle
triangle = Triangle(name='triangle', base=5, height=6, angles=3, side_a=2, side_b=4, side_c=5)
# Инициализация triangle.area
triangle.area = Triangle.get_triangle_area(base=5, height=6)
# Инициализация triangle.perimeter
triangle.perimeter = Triangle.get_triangle_per(4, 5, 7)

