"""Тесты треугольника"""


def test_triangle_area(triangle):
    assert triangle.get_area() == 15


def test_triangle_perimeter(triangle):
    assert triangle.get_perimeter() == 11


def test_add_area_triangle(triangle, rectangle):
    assert triangle.add_area(rectangle) == 50.0


def test_is_instance_not_figure(triangle, example):
    assert not triangle.add_area(example)
