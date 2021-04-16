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
