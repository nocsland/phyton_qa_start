from home_work_1.source.Figure import Figure


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

    def get_triangle_area(self):
        """Площадь треугольника"""
        triangle_area = 0.5 * self.base * self.height
        return triangle_area

    def get_triangle_per(self):
        """Периметр треугольника"""
        triangle_perimeter = self.side_a + self.side_b + self.side_c
        return triangle_perimeter

    def add_area_triangle(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            total_area = figure.area + self.area
            return total_area
        else:
            print('передан неправильный класс')


# Инициализация объекта triangle
triangle = Triangle(name='triangle', base=5, height=6, angles=3, side_a=2, side_b=4, side_c=5)
# Инициализация и передача из данных из функции для triangle.area
triangle.area = Triangle.get_triangle_area(triangle)
# Инициализация и передача из данных из функции для triangle.perimeter
triangle.perimeter = Triangle.get_triangle_per(triangle)


