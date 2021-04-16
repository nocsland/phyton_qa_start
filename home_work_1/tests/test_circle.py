"""Тесты окружности"""
from home_work_1.source.Circle import circle
from home_work_1.source.Circle import Circle
from home_work_1.source.Triangle import triangle
from home_work_1.source.Example import example

def test_circle_area():
    assert Circle.get_circle_area(circle) == 226.1946710584651


def test_circle_length():
    assert Circle.get_circle_length(circle) == 37.69911184307752

# Сумма площадей
def test_add_area_circle():
    assert Circle.add_area_circle(circle, triangle) == 241.1946710584651


# Объект не фигура
def test_object_not_figure():
    assert not Circle.add_area_circle(circle, example)
