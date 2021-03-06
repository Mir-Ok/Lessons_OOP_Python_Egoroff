''' Методы __eq__ и __hash__
    Они связаны между собой, поэтому снова повторим первый '''


class Point:
    pass


''' Любое значение в Питоне представляет из себя объект. 
    При создании объект получает некоторое поведение, а так же возможность их сравнения по их id 
    Что делать, если мы хотим сравнивать по другим атрибутам? 
    
    Для начала, поясним что экземпляры поддерживают операцию hash(). 
    Вкратце это некоторая математическая, которая принимает наш объект и преобразует его в некоторое занчение.
    Обратно из него объект уже не получить, это одностороннее 
    Сейчас важно, что в момоент создания объект имеет id и может быть хеширован '''

p0 = Point()
print(hash(p0))  # --> 117955479263 объект хешируется

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # объекты равны, если выполнены все три проверки
    def __eq__(self, other):
        return isinstance(other, Point2) and self.x == other.x and self.y == other.y

p1 = Point2(1, 2)
p2 = Point2(1, 2)
print(id(p1))  # --> 1458879884784
print(id(p2))  # --> 1458879902624
print(p1==p2)  # --> True та как коорд. совпадают, хотя объекты разные по id

''' но после переопределения метода __eq__ перестанет работать функция hash(), потому
    что раньше он считался id. У равных объектов был одинаковый id а мы сделали так, 
    что даже разные объекты могут быть равны, но по другим параметрам 
    
    Хеш можно найти не у всех объектов, атолько у неизменяемых. Числа, строки, кортежи. А у
    списков его нет. Объекты бывают hashable and unhashable.
    hashable используеются в словарях и множествах в качестве ключа  '''

d = {}
d[1] = 100   # --> запускается без ошибок
# d[p2] = 100  # --> TypeError: unhashable type: 'Point2'

''' Иногда нам нужно, чтобы объект стал хешируемым и получил возможность 
    быть ключом словаря или множества. Поэтому к переопределенному методу __eq__ добавим
    определение __hash__ '''

class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # объекты равны, если выполнены все три проверки
    def __eq__(self, other):
        return isinstance(other, Point3) and self.x == other.x and self.y == other.y

    # возвращаем значение от кортежа(!), который состоит из нужного нам. мы явно указали, от чего считать
    def __hash__(self):
        return hash((self.x, self.y))

p5 = Point3(3, 4)
p6 = Point3(3, 4)
p7 = Point3(30, 40)

print(p5==p6)  # --> True
print(p5==p7)  # --> False

# хеш-значения стали равны, так как мы берем их от кортежа координат, а он идентичен
print(hash(p5))  # --> 1079245023883434373
print(hash(p6))  # --> 1079245023883434373

# отличается
print(hash(p7))  # --> 3342721321007327999

r = {}
r[p5] = 100 # --> запускается без ошибок даже с ключом в виде объекта класса



# total_ordering
# Чтобы не реализовывать все магические методы сравнения, можно использовать декоратор functools.total_ordering,
# который позволяет  сократить код, реализовав только методы __eq__ и __lt__

from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


acc1 = Account(10)
acc2 = Account(20)
print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
print(acc1 != acc2)
print(acc1 >= acc2)
print(acc1 <= acc2)