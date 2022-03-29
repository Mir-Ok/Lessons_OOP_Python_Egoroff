''' Магические методы будут срабатывать, когда я к своему объекту вызову фунции len()
    или abs() соотв.
    Проблема в том, что не все типы объектов поддерживают функции выше, у каждого типа прописан свой магический метод,
    так как это тоже класcы, но предустановленные '''

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

print((78).__abs__())  # -->  78 демонстрация, что у чисел есть предустановленный метод

class Person2:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # пропишем функцию, которая возвращает суммарную длину имени и фамилии
    def __len__(self):
        return len(self.name + self.surname)

leo = Person2('leo', 'Kats')
print(len(leo))  # --> 7
loe = Person2('1', '20')
print(len(loe))  # --> 3 количество символов

# print(abs(loe))  # --> TypeError: bad operand type for abs(): 'Person2'

''' Реализуем второй метод '''

class Otrezok:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    # пропишем функцию, которая возвращает суммарную длину имени и фамилии
    def __len__(self):
        return self.x2 - self.x1

first = Otrezok(5,9)
print(len(first))  # --> 4

''' Если же мы создадим отрезок, у которого второе значение меньше первого,
    мы получим ошибку '''

second = Otrezok(9,4)
# print(len(second))  # --> ValueError: __len__() should return >= 0

''' Для избавления от минуса внесем дополнения '''

class Otrezok2:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    # при вызове обратится к функции расчета модуля разности и подаст туда принятое знаение
    def __len__(self):
        return abs(self)

    # пропишем функцию, которая возвращает модуль разницы
    def __abs__(self):
        return abs(self.x2 - self.x1)

third = Otrezok2(9,4)
print(len(third))  # --> 5

fourth = Otrezok2(2,4)
print(len(fourth))  # --> 2

# можно вызвать напрямую
print(fourth.__abs__())  # --> 2