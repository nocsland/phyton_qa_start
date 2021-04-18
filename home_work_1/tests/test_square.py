"""Тесты квадрата"""
from home_work_1.source.Square import Square


def test_square_area(square):
    assert Square.get_square_area(square) == 36


def test_square_perimeter(square):
    assert Square.get_square_perimeter(square) == 24


def test_add_area_square(square, circle):
    assert Square.add_area(square, circle) == 262.19467105846513


def test_object_not_figure(square, example):
    assert not Square.add_area(square, example)
