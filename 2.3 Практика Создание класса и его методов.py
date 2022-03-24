# Практика. Класс Point(x,y)

class Point:

    # определим конструктор класса? при вызове класса сразу получим 2 готовых атрибута
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

# Проверим работу
p1 = Point(3,4)  # без аргументов не вызывается
print(p1.x)  # --> 3

''' Изменим класс, чтобы по умолчанию точка была в начале координат '''

class Point:

    # появились значения по умолчанию
    def __init__(self, coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y

''' Добавим точкам поведение, чтобы они могли перемещаться '''

class Point:

    # появились значения по умолчанию
    def __init__(self, coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y

    # здесь описывается новое поведение
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # здесь описывается еще одно новое поведение
    def go_home(self):
        self.x = 0
        self.y = 0

''' Обратим внимание, что у всех методов одинакова логика работы, они меняют координаты
    точке, но  один вызывается сам, а два мы вызываем вручную.
    Перепишем так, чтобы использовать один метод внутри другого
    
    Это принцип написания кода DRY (don't repeat youtself) '''

class Point:

    # появились значения по умолчанию
    def __init__(self, coord_x = 0, coord_y = 0):
        self.move_to(coord_x, coord_y)

    # здесь описывается новое поведение
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # метод в методе
    def go_home(self):
        self.move_to(0, 0)

    # Добавим еще один метод, который поможет нам выводит на печать экземпляр класса в нормальном
    # виде, а не его адрес

    def print_point(self):
        print(f'Точка с координатами {self.x},{self.y }')

''' Пока что все описанные методы работали только с одним экземпляром класса.
    Давайте напишем метод, который работает с несколькими 
    '''

class Point:

    def __init__(self, coord_x = 0, coord_y = 0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами {self.x},{self.y }')

    # новый метод
    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Объект должен принадлежать классу точка ')
        else:
            ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5

''' Дополним класс атрибутом, который будет виден всем методам  '''

class Point:

    list_points = []

    def __init__(self, coord_x = 0, coord_y = 0):
        self.move_to(coord_x, coord_y)
        # обратмся через класс и пополним список при каждой новой инициализации
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами {self.x},{self.y }')

    # новый метод
    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Объект должен принадлежать классу точка ')
        else:
            ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5