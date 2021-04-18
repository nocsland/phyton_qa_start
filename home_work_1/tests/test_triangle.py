"""Тесты треугольника"""
from home_work_1.source.Triangle import Triangle


def test_triangle_area(triangle):
    assert triangle.get_triangle_area() == 15


def test_triangle_perimeter(triangle):
    assert triangle.get_triangle_per() == 11


def test_add_area_triangle(triangle, rectangle):
    assert Triangle.add_area(self=triangle, figure=rectangle) == 50.0


<<<<<<< HEAD
def test_is_instance_not_figure(triangle, example):
    assert not Triangle.add_area(triangle, example)
=======
# Объект не фигура
def test_object_not_figure():
    assert not Triangle.add_area_triangle(triangle, example)
>>>>>>> 8eb26354638c0fdd9e8c789b063a15f665c69b3c
