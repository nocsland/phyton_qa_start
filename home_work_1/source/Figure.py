class Figure:
    """Базовый класс"""
    def __init__(self, name, angles):
        self.name = name
        self.angles = angles
        self.area = self.add_area(self)

    def add_area(self, figure):
        """Метод вычисления суммы площадей фигур"""
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            print('Передан неправильный класс')
