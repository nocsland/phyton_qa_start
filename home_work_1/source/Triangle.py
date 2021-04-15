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


def add_area(figure):
    """Метод вычисления суммы площадей фигур"""
    if isinstance(figure, Figure):
        total_area = figure.area + triangle.area
        return total_area
    else:
        print('передан неправильный класс')


# Инициализация объекта triangle
triangle = Triangle(name='triangle', base=5, height=6, angles=3, side_a=2, side_b=4, side_c=5)

# Площадь треугольника
triangle.area = 0.5 * triangle.height * triangle.base

# Периметр треугольника
triangle.perimeter = triangle.side_a + triangle.side_b + triangle.side_c

