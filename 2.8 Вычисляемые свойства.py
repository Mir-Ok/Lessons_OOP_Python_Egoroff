''' Как можно класс property() использовать в качестве вычисляемых атрибутов

    Проблема: есть класс Square(), хранящий в себе информацию про квадрат, его сторона '''

class Square:

    def __init__(self,s):
        self.side = s

    # метод, вычисляющий площадь
    def area(self):
        return self.side ** 2

a = Square(5)
print(a.area())  # --> 25

''' Если подумать, то в ООП у нас есть атрибуты, они же переменные и методы, 
    что как правило является функцией.
    
    Что такое площадь? Это атрибут, то есть переменная. И вроде как мы не должны ее вызывать как метод
    Но мы можем поменять сторону квадрата и тем самым вызвать изменение площади
     
    В нашем случае площадь должна быть вычисляемым свойством, зависящим от размера '''

class Square2:

    def __init__(self,s):
        self.side = s

    # метод, вычисляющий площадь, ставший свойством
    @property
    def area(self):
        return self.side ** 2

a = Square2(21)
print(a.area)  # --> 441, ВАЖНО вызываем без () как свойство, которое вычисляемое

''' Вроде хорошо, но теперь есть проблема с тем, что вычисляемое значение вычисляется раз за разом, 
    и если операций много - звешивает систему
    
    Как решить? Создадим приватную переменную __area и зададим ей по умолчанию None/
    И вводим условие, что пересчитываем площадь только если она изменилась '''

class Square3:

    def __init__(self,s):
        self.side = s
        self.__area = None

    # метод, вычисляющий площадь, ставший свойством
    @property
    def area(self):
        if self.__area is None:
            print('Calculate area')
            self.__area = self.side **2
        return self.__area

c = Square3(8)
print(c.area)  # --> Calculate area   64

''' Текущие изменения привели  тому, что площадь не считается каждый раз, но если меняется длина стороны квадрата,
    то перерасчета тоже не происходит 
    Добавим геттер и сеттер,  которые отреагируют на изменение длины стороны, 
    и зададим возврат None в этом же случае для __area '''

class Square4:

    def __init__(self,s):
        self.__side = s  # сделаем приватной
        self.__area = None

    @property
    def side(self):  # добавим геттер, название  side()
        return self.__side

    @property
    def side(self, value):   # добавим сеттер, название  side()
        self.__side = value  # меняющий значение стороны на вновь введенный
        self.__area = None   # и восстановим None

    @property
    def area(self):
        if self.__area is None:
            print('Calculate area')
            self.__area = self.__side **2
        return self.__area

d = Square4(8)
print(d.area)  # --> Calculate area   64

e = Square4(9)
print(e.area)  # --> Calculate area   81