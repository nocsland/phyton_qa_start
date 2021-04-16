"""Тесты треугольника"""
from home_work_1.source.Triangle import Triangle
from home_work_1.source.Triangle import triangle
from home_work_1.source.Circle import circle
from home_work_1.source.Example import example


# Площадь треугольника
def test_triangle_area():
    assert Triangle.get_triangle_area(triangle) == 15


# Периметр треугольника
def test_triangle_perimeter():
    assert Triangle.get_triangle_per(triangle) == 11


# Сумма площадей
def test_add_area_triangle():
    assert Triangle.add_area_triangle(triangle, circle) == 241.1946710584651


# Объект не фигура
def test_object_not_figure():
    assert not Triangle.add_area_triangle(triangle, example)
#
#
# def test_triangle_is_figure():
#     assert Figure.is_triangle_figure(Figure.Triangle)
#
#
# # Тесты на прямоугольник
# def test_area_rectangle():
#     assert Figure.rectangle_area(5, 8) == 40
#
#
# def test_rectangle_per():
#     assert Figure.rectangle_per(2, 5) == 14
#
#
# def test_add_area_rectangle():
#     assert Figure.add_area_triangle(Figure.Triangle) == 30.0
#
#
# def test_rectangle_is_figure():
#     assert Figure.is_rectangle_figure(Figure.Rectangle)


# # Тесты на квадрат
# def test_area_square():
#     assert Figure.square_area(5) == 25
#
#
# def test_square_per():
#     assert Figure.square_per(5) == 20
#
#
# def test_add_area_square():
#     assert Figure.add_area_triangle(Figure.Rectangle) == 23
#
#
# def test_square_is_figure():
#     assert Figure.is_square_figure(Figure.Square)
#
#
# # Тесты на окружность
# def test_area_circle():
#     assert Figure.circle_area(5) == 78.53981633974483
#
#
# def test_circle_length():
#     assert Figure.circle_length(8) == 50.26548245743669
#
#
# def test_add_area_circle():
#     assert Figure.add_area_circle(Figure.Circle) == 100.53096491487338
#
#
# def test_circle_is_figure():
#     assert Figure.is_circle_figure(Figure.Circle)
#
#     assert not Figure.is_circle_figure(Figure.Obj)
