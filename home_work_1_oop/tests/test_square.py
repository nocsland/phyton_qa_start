"""Тесты квадрата"""


def test_square_area(square):
    assert square.get_area() == 36


def test_square_perimeter(square):
    assert square.get_perimeter() == 24


def test_add_area_square(square, circle):
    assert square.add_area(circle) == 262.19467105846513


def test_object_not_figure(square, example):
    assert not square.add_area(example)
