"""Тесты прямоугольника"""


def test_rectangle_area(rectangle):
    assert rectangle.get_area() == 35


def test_triangle_perimeter(rectangle):
    assert rectangle.get_perimeter() == 24


def test_add_area_rectangle(rectangle, square):
    assert rectangle.add_area(square) == 71


def test_is_instance_not_figure(rectangle, example):
    assert not rectangle.add_area(example)
