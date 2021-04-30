"""Тесты окружности"""


def test_circle_area(circle):
    assert circle.get_area() == 226.1946710584651


def test_circle_perimeter(circle):
    assert circle.get_perimeter() == 37.69911184307752


def test_add_area_circle(circle, triangle):
    assert circle.add_area(triangle) == 241.1946710584651


def test_is_instance_not_figure(circle, example):
    assert not circle.add_area(example)
