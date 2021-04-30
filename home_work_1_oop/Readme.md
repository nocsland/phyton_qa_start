Домашнее задание

Реализуем ООП на практике
Цель:

Научиться работать с парадигмой ООП, потренировать объектное мышление, поучиться писать тесты.

Создать базовый класс геометрической фигуры (Figure). Реализовать на его основе классы геометрических фигур
Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).

1 Часть.

Каждая фигура должна иметь атрибуты: 
name - название фигуры, area (вычисляемое!) - площадь, angles - количество углов 
perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности)

Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур.
Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру
и возвращать сумму площадей этих фигур. Если передана не геометрическая фигура,
то нужно выдавать ошибку и сообщать что передан неправильный класс.

Опционально (необязательно): Запретить создавать инстансы базового класса Figure.

2 Часть.

Написать тесты с использованием pytest на эти классы. По одному тесту на каждый метод каждой фигуры. 
Т.е. будет четыре тестовых модуля по 5 тестов на каждый. Можно написать и больше. :)

Задача: Потренировать объектно-ориентированное мышление, и написание тестов на собственный код.
Критерии оценки:

    Будет оцениваться глубина использования парадигмы ООП.
    Встроенные декораторы, наследование, отсутствие дублирования кода.
    Если какой-то метод выполняет одно и тоже во всех классах наследниках, 
    то он должен принадлежать родтельскому классу.
    Задание сдавать в формате pull-request.

Рекомендуем сдать до: 15.04.2021