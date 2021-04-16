from home_work_1.source.Rectangle import Rectangle
from home_work_1.source.Rectangle import rectangle
from home_work_1.source.Triangle import triangle
from home_work_1.source.Example import example


# Площадь прямоугольника
def test_rectangle_area():
    assert Rectangle.get_rectangle_area(rectangle) == 35


# Периметр прямоугольника
def test_triangle_perimeter():
    assert Rectangle.get_rectangle_perimeter(rectangle) == 24


# Сумма площадей
def test_add_area_rectangle():
    assert Rectangle.add_area_rectangle(rectangle, triangle) == 50.0


# Объект не фигура
def test_object_not_figure():
    assert not Rectangle.add_area_rectangle(rectangle, example)
