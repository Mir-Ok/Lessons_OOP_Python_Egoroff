class Person:

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')


class Doctor(Person):
    pass


p = Person()
print(p.breathe())  # --> Человек дышит находит метод у себя

d = Doctor()
print(d.breathe())  # --> Человек дышит ... находит метод у родительского класса

''' Однако мы можем переопределить у потомка класс, сохранив название и поменяв его поведение '''

class Person1:

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')


class Doctor1(Person1):
    def breathe(self):
        print('Доктор дышит')

p1 = Person1()
print(p1.breathe())  # --> Человек дышит находит метод у себя

d1 = Doctor1()
print(d1.breathe())  # --> Доктор дышит ... находит плявился и у него самого

''' Внутри дочернего класса мы можем менять родительские атрибуты (переменные) '''

''' Поговорим про переопределение методов базового класса 
    Любопытно. что при добавлении метода __init__ дочерний класс и родительский 
    вызовут его по одному разу. Это обусловлено цепочкой наследования  '''


class Person2:

    def __init__(self, name):
        self.name = name
        print('__init__ Person')
    def breathe(self):
        print('Человек дышит')
    def walk(self):
        print('Человек гуляет')

class Doctor2(Person2):
    def breathe(self):
        print('Доктор дышит')

print(' --- ')
p2 = Person2('Joe')
print(p2.breathe())

d2 = Doctor2('Lex')
print(d2.breathe())

print(p2, d2)  # <__main__.Person3 object at 0x000002B4BD0F7310> <__main__.Doctor3 object at 0x000002B4BD0F7370>

''' __init__ Person
    Человек дышит
    
    __init__ Person
    Доктор дышит  '''

''' Поменяем немного, добавим доктору метод __str__ '''


class Person3:

    def __init__(self, name):
        self.name = name
        print('__init__ Person')

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')


class Doctor3(Person3):
    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Доктор {self.name}'


print(' --- ')
p3 = Person3('Joe')
print(p3.breathe())  # __init__ Person   Человек дышит

d3 = Doctor3('Lex')
print(d3.breathe())  # __init__ Person   Доктор дышит

print(p3, d3)  # <__main__.Person3 object at 0x000001F3AE6273A0> Доктор Lex

''' Замена произошла потому что у класса Person3 нет определенного метода __str__ и класс
    вынужден брать его у object
    А у класса доктор он есть, прописанный, и запускается именно он, просторанство имен соотв. 
    
    Если же мы поднимем определение метода в родительский класс, перенесем из Doctor в Person?
    то с нормальным названем будут выводиться оба экземпляра, потому что и родитель, и наследник
    теперь имеют прописанный метод 
    Для кастомизации переопределим в обоих классах '''

class Person4:

    def __init__(self, name):
        self.name = name
        print('__init__ Person')

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')

    def __str__(self):
        return f'Персона {self.name}'

class Doctor4(Person4):
    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Доктор {self.name}'


print(' --- ')
p4 = Person4('Joe')  # __init__ Person
d4 = Doctor4('Lex')  # __init__ Person

print(p4, d4)  # Персона Joe Доктор Lex

''' Дополним функциональность еще немного '''

class Person5:

    def __init__(self, name):
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек гуляет')

    def __str__(self):
        return f'Персона {self.name}'

    def sleep(self):
        print('Человек спит')

    # демонстрация того, что один метод может вызывать другие
    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

class Doctor5(Person5):
    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Доктор {self.name}'


print(' --- ')
p5 = Person5('Joe')  # __init__ Person
d5 = Doctor5('Lex')  # __init__ Person

print(p5.combo())  #  Человек дышит  Человек гуляет  Человек спит
print(d5.combo())  #  Доктор  дышит  Человек гуляет  Человек спит - переопределен только один