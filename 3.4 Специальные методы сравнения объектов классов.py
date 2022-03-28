''' Магические методы сравнения/ без них сравнение не поддерэивается

    __eq__ отвечает за ==
    __ne__ отвечает за !=
    __lt__ отвечает за <
    __le__ отвечает за <=
    __gt__ отвечает за >
    __ge__ отвечает за >=   '''


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b


# v = Rectangle(1, 2)
# r = Rectangle(4, 5)
# v > r  # --> TypeError: '>' not supported between instances of 'Rectangle' and 'Rectangle'
# потому что идет сравнение не периметров, а их id

class Rectangle2:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):  # в other значение, с которым сравнивается
        print('eq called')
        if isinstance(other, Rectangle2):
            return self.a == other.a and self.b == other.b

    @property
    def area(self):  # создаем метод расчета площади и превращаем его в свойство
        return self.a + self.b

    def __lt__(self, other):  # де - less than
        print('lt called')
        if isinstance(other, Rectangle2):
            return self.area < other.area  # пользуемся созданным свойством
        elif isinstance(other, (int, float)):
            return self.area < other


# v = Rectangle2(1, 2)
# r = Rectangle2(4, 5)
# print(v == r)  # --> eq called   False
# print(v < r)  # --> lt called   True
# print(v > r)  # --> lt called   False

''' Мы можем сравнить r > 15, но запрос 15 > r вызовет ошибку.
    Но в ситуации сравнения v < r он догадается повернуть выражение '''

''' Добавим нестрогое сравнение, но избежим дублирования кода за счет прописанных
    ранее магических методов   '''


class Rectangle3:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):  # в other значение, с которым сравнивается
        print('__eq__ called')
        if isinstance(other, Rectangle3):
            return self.a == other.a and self.b == other.b

    @property
    def area(self):  # создаем метод расчета площади и превращаем его в свойство
        return self.a + self.b

    def __lt__(self, other):  # де - less than
        print('__lt__ called')
        if isinstance(other, Rectangle3):
            return self.area < other.area  # пользуемся созданным свойством
        elif isinstance(other, (int, float)):
            return self.area < other

    # обращаемся к методам __eq__ и __lt__, для истины достаточно истинности одного из них
    def __le__(self, other):
        return self == other or self < other

v = Rectangle3(4, 5)
r = Rectangle3(4, 6)
print(v <= r)  # --> eq called   True, второй метод даже не потребовался, он не запускался

''' Раз равенство реализовано, то неравенство Питон укажет сам, от обратного
    Полная реализация всех 6 методов обычно не нужна, они друг друга подхватывают '''
print(v != r)