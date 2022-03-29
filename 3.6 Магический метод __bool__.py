''' Магические методы __bool__

    Любое значение представляет собой объект, и каждый из них имеет свойство правдивости
    (правда/ложь), чтобы узнать, к какому из них - вызываем bool()
    Числа все ИСТИНА, 0 - ЛОЖЬ
    Строки, списки, любые коллекции непустые - ИСТИНА, пустые - ЛОЖЬ
     '''


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(2, 3)
print(bool(p1))  # --> True Если не определен __bool__, то Питон смотрит в __len__

''' Определим __len__ '''


class Point2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ called')
        return abs(self.x - self.y)

p2 = Point2(2, 3)
print(bool(p2))  # --> __len__ called   True, так как не ноль
p3 = Point2(3, 3)
print(bool(p3))  # --> __len__ called   False, так как ноль

''' Если __len__ и __bool__ не определены, то экземпляры всегда правдивы! '''


class Point3:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__ called')
        return abs(self.x - self.y)
    def __bool__(self):
        print('__bool__ called')
        # записываем условие, при котором выдается ИСТИНА
        return self.x != 0 or self.y != 0

p4 = Point3(-1, 0)  # -->  __bool__ called  True
print(bool(p4))

p5 = Point3(0, 0)  # -->  __bool__ called  True
print(bool(p5))

''' Можно обращаться к функциям и пямо, и косвенно '''
if p4:
    print('Истина')  # -->  __bool__ called  Истина

