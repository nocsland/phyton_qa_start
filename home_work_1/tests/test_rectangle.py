"""Тесты прямоугольника"""
from home_work_1.source.Rectangle import Rectangle


def test_rectangle_area(rectangle):
    assert Rectangle.get_rectangle_area(rectangle) == 35


def test_triangle_perimeter(rectangle):
    assert Rectangle.get_rectangle_perimeter(rectangle) == 24


def test_add_area_rectangle(rectangle, square):
    assert Rectangle.add_area(rectangle, square) == 71


def test_is_instance_not_figure(triangle, example):
    assert not Rectangle.add_area(triangle, example)
