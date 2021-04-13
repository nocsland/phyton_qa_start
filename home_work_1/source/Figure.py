"""Исходный код"""

from math import pi


# Создаем классы
# Класс Example исключительно для проверки
class Example:
    name = None


Obj = Example()


class Figure:
    # объявим атрибуты класса
    name = None
    area = 0
    angles = 0
    perimeter = 0


# Создаем объекты
Triangle = Figure()
Rectangle = Figure()
Square = Figure()
Circle = Figure()


# Методы для треугольника


# Площадь треугольника
def triangle_area(b, h):
    tr_area = 0.5 * b * h
    # print(f'Площадь треугольника c основанием {b} и высотой {h} равна: {tr_area}')
    return tr_area


# Периметр треугольника
def triangle_per(a, b, c):
    tr_per = a + b + c
    # print(f'Периметр треугольника со сторонами {a}, {b}, {c} равен {tr_per}')
    return tr_per


# Добавить к площади треугольника, площадь другой фигуры
def add_area_triangle(figure):
    figures_area = figure.area + Triangle.area
    # print(f'Сумма площади треугольника и другого объекта равна  {figures_area}')
    return figures_area


# Проверить что треугольник это объект класса Figure
def is_triangle_figure(figure):
    if isinstance(figure, Figure):
        return True
    else:
        return print('Переданный объект не является элементом класса Figure')


# Площадь прямоугольника
def rectangle_area(length_rect, width_rect):
    rect_area = length_rect * width_rect
    # print(f'Площадь прямоугольника со сторонами {width_rect} и {length_rect} равна: {rect_area}')
    return rect_area


# Периметр прямоугольника
def rectangle_per(length_rect, width_rect):
    rect_per = (length_rect + width_rect) * 2
    # print(f'Периметр прямоугольника со сторонами {width_rect} и {length_rect} равен: {rect_per}')
    return rect_per


# Добавить к площади прямоугольника, площадь другой фигуры
def add_area_rectangle(figure):
    figures_area = figure.area + Rectangle.area
    # print(f'Сумма площади треугольника и другого объекта равна  {figures_area}')
    return figures_area


# Проверить что прямоугольник это объект класса Figure
def is_rectangle_figure(figure):
    if isinstance(figure, Figure):
        return True
    else:
        return print('Переданный объект не является элементом класса Figure')


# Площадь квадрата
def square_area(square_side):
    sq_area = square_side ** 2
    # print(f'Площадь квадрата со стороной {square_side} равна: {sq_area}')
    return sq_area


# Периметр квадрата
def square_per(square_side):
    sq_per = (square_side * 4)
    # print(f'Периметр квадрата со стороной {square_side} равен: {sq_per}')
    return sq_per


# Добавить к площади квадрата, площадь другой фигуры
def add_area(figure):
    figures_area = figure.area + Square.area
    return figures_area


# Проверить что квадрат это объект класса Figure
def is_square_figure(figure):
    if isinstance(figure, Figure):
        return True
    else:
        return print('Переданный объект не является элементом класса Figure')


# Площадь круга
def circle_area(circle_rad):
    cir_area = pi * circle_rad ** 2
    # print(f'Площадь круга c радиусом {circle_rad} равна: {cir_area}')
    return cir_area


# Длинна окружности
def circle_length(circle_rad):
    cir_length = 2 * pi * circle_rad
    # print(f'Длина окружности c радиусом {circle_rad} равна: {cir_length}')
    return cir_length


# Добавить к площади круга, площадь другой фигуры
def add_area_circle(figure):
    figures_area = figure.area + Circle.area
    # print(f'Сумма площади круга и другого объекта равна  {figure_area}')
    return figures_area


# Проверить что круг это объект класса Figure
def is_circle_figure(figure):
    if isinstance(figure, Figure):
        return True
    else:
        return print('Переданный объект не является элементом класса Figure')


# Атрибуты треугольника
Triangle.angles = 3
Triangle.name = 'Triangle'
Triangle.area = triangle_area(5, 6)
Triangle.perimeter = triangle_per(2, 4, 5)

# Атрибуты прямоугольника
Rectangle.angles = 4
Rectangle.name = 'Rectangle'
Rectangle.area = rectangle_area(4, 2)
Rectangle.perimeter = rectangle_per(2, 4)

# Атрибуты прямоугольника
Square.angles = 4
Square.name = 'Square'
Square.area = square_area(4)
Square.perimeter = square_per(5)

# Атрибуты круга
Circle.angles = 0
Circle.name = 'Circle'
Circle.area = circle_area(4)
Circle.perimeter = circle_length(5)
