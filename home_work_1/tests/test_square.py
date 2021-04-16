from home_work_1.source.Square import Square
from home_work_1.source.Square import square
from home_work_1.source.Rectangle import rectangle
from home_work_1.source.Example import example


# Площадь прямоугольника
def test_square_area():
    assert Square.get_square_area(square) == 36


# Периметр прямоугольника
def test_square_perimeter():
    assert Square.get_square_perimeter(square) == 24


# Сумма площадей
def test_add_area_square():
    assert Square.add_area_square(square, rectangle) == 71.0


# Объект не фигура
def test_object_not_figure():
    assert not Square.add_area_square(square, example)
