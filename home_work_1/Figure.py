"""Создать базовый класс геометрической фигуры (Figure).
Реализовать на его основе классы геометрических фигур:
Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle)."""


# Создаем класс
class Figure:
    name = None
    area = 0
    angles = 0
    perimeter = 0


# Создаем объекты
Triangle = Figure()
Rectangle = Figure()
Square = Figure()
Circle = Figure()


def triangle_area(o, h):
    tr_area = 0.5 * o * h
    print(f'Площадь треугольника равна: {tr_area}')
    return tr_area


def triangle_per(a, b, c):
    tr_per = a + b + c
    print(f'Периметр треугольника равен: {tr_per}')
    return tr_per


# Атрибуты треугольника
Triangle.angles = 3
Triangle.name = 'Triangle'
Triangle.area = triangle_area(5, 6)
Triangle.perimeter = triangle_per(2, 4, 5)
