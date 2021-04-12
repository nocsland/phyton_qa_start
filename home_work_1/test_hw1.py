import Figure


# Тесты на треугольник
def test_area_triangle():
    assert Figure.triangle_area(5, 6) == 15


def test_triangle_per():
    assert Figure.triangle_per(2, 4, 5) == 11


def test_add_area_triangle():
    assert Figure.add_area_triangle(Figure.Circle) == 65.26548245743669


def test_triangle_is_figure():
    assert Figure.is_triangle_figure(Figure.Triangle)
