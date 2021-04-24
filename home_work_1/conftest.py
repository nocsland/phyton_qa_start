import pytest
from home_work_1.source.Triangle import Triangle
from home_work_1.source.Circle import Circle
from home_work_1.source.Example import Example
from home_work_1.source.Square import Square
from home_work_1.source.Rectangle import Rectangle


@pytest.fixture
def circle():
    return Circle(name='circle', angles=0, radius=6)


@pytest.fixture
def triangle():
    return Triangle(name='triangle', base=5, height=6, angles=3, side_a=2, side_b=4, side_c=5)


@pytest.fixture
def rectangle():
    return Rectangle(name='rectangle', angles=4, length=5, width=7)


@pytest.fixture
def square():
    return Square(name='square', angles=4, length=6, width=6)


@pytest.fixture
def example():
    return Example()
