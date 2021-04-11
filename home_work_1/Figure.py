"""Создать базовый класс геометрической фигуры (Figure).
Реализовать на его основе классы геометрических фигур:
Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).

Часть 1
Каждая фигура должна иметь атрибуты: name - название фигуры, area (вычисляемое!) - площадь,
angles - количество углов perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности)
Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур.
Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру
и возвращать сумму площадей этих фигур. Если передана не геометрическая фигура, то
нужно выдавать ошибку и сообщать что передан неправильный класс.
Опционально (не обязательно): Запретить создавать инстансы базового класса Figure.

Часть 2
Написать тесты с использованием pytest на эти классы. По одному тесту на каждый метод каждой фигуры.
Т.е. будет четыре тестовых модуля по 5 тестов на каждый. Можно написать и больше. :)
Задача: Потренировать объектно-ориентированное мышление, и написание тестов на собственный код.
Критерии оценки:
    Будет оцениваться глубина использования парадигмы ООП.
    Встроенные декораторы, наследование, отсутствие дублирования кода.
    Если какой-то метод выполняет одно и тоже во всех классах наследниках,
    то он должен принадлежать родтельскому классу.
    Задание сдавать в формате pull-request.
Рекомендуем сдать до: 15.04.2021"""

from math import pi


# Создаем класс
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
    print(f'Площадь треугольника равна: {tr_area}')
    return tr_area


# Периметр треугольника
def triangle_per(a, b, c):
    tr_per = a + b + c
    print(f'Периметр треугольника равен: {tr_per}')
    return tr_per


# # Добавить площадь  фигуры
# def add_area(diff_area):
#     ad_area = diff_area + triangle_area
#     return ad_area
#     if not isinstance(diff_area, Figure):
#         print('объект не является фигурой')
#


# Площадь прямоугольника
def rectangle_area(length_rect, width_rect):
    rect_area = length_rect * width_rect
    print(f'Площадь прямоугольника равна: {rect_area}')
    return rect_area


# Периметр прямоугольника
def rectangle_per(length_rect, width_rect):
    rect_per = (length_rect + width_rect) * 2
    print(f'Периметр прямоугольника равен: {rect_per}')
    return rect_per


# Площадь квадрата
def square_area(square_side):
    sq_area = square_side ** 2
    print(f'Площадь квадрата равна: {sq_area}')
    return sq_area


# Периметр квадрата
def square_per(square_side):
    sq_per = (square_side * 4)
    print(f'Периметр квадрата равен: {sq_per}')
    return square_side


# Площадь круга
def circle_area(circle_rad):
    cir_area = pi * circle_rad ** 2
    print(f'Площадь круга равна: {cir_area}')
    return cir_area


# Длинна окружности
def circle_length(circle_rad):
    cir_length = 2 * pi * circle_rad
    print(f'Длина окружности равна: {cir_length}')
    return cir_length


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
