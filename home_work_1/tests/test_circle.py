"""Тесты окружности"""
from home_work_1.source.Circle import Circle


def test_circle_area(circle):
    assert circle.get_circle_area() == 226.1946710584651


def test_circle_length(circle):
    assert circle.get_circle_length() == 37.69911184307752


def test_add_area_circle(circle, triangle):
    assert Circle.add_area(self=circle, figure=triangle) == 241.1946710584651


def test_is_instance_not_figure(circle, example):
    assert not Circle.add_area(self=circle, figure=example)
