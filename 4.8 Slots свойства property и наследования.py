class Rectangle:
    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * + self.height


t1 = Rectangle(3, 4)

print(t1.width)  # --> 3
print(t1.height)  # --> 4

print(t1.perimetr)  # --> 14
print(t1.area)  # --> 12

''' Обратим внимание, что свойства, заданные через переназначение (вычисляемые), 
    доступны, хотя их нет в __slots__ 
    
    И редактировать их нельзя, так как определен только геттер '''

# t1.perimetr = 25
# print(t1.perimetr)  # AttributeError: can't set attribute

''' Рассмотрим, как мы можем защитить переменнеы в слотах '''


class Rectangle2:
    __slots__ = '__width', 'height'  # добавляем __ именно здесь

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


t2 = Rectangle2(5, 8)  # --> setter called
print(t2.width)  # --> 5
print(t2.height)  # --> 8

''' Рассмотрим работу наследования в слотах 
    
    Важно помнить, что у дочерних классов есть __dict__, а значит возможность
    создавать переменные, обращаться к ним, удалять
     
    Если же мы слотируем клас,то етсь пропишем __slots__, то оно расширит набор родителя
    Мы допишем парочку, и унаследуем парочку, итого будет 4, дублировать не надо в дочернем 
    
    Если не хотим расширять. то подаем в слот дочернего пустой кортеж 
    __slots__ =  tuple()   '''


class Square(Rectangle2):
    __slots__ = 'color'

    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color


s1 = Square(8, 8, 'red')  # --> setter called
# print(s1.__dict__)  # снова потеряли словарь AttributeError: 'Square' object has no attribute '__dict__'
