class Doctor:
    def can_cure(self):
        print('Я могу лечить')
    def can_breathe(self):
        print('Я могу дышать')


class Architect:
    def can_build(self):
        print('Я могу строить здания')
    def can_breathe(self):
        print('Я могу дышать')

''' У каждого персонажа есть свое умение и одно повторяющееся - умение ходить.
    А если их будет 10? Дышать, кушать, гулять ...
    
    Чтобы собрать в одном место все повторы и убрать дубликаты - создадим класс, 
    содержащий в себе базовые навыки (атрибуты и методы) и настроим так, чтобы другие классы
    могли получать их при создании, в дополнении к своим собственным методам и атрибутам '''

class Person:  # базовый класс, родитель
    def can_breathe(self):
        print('Я могу дышать')

class Doctor1(Person):  # подкласс, в скобках прописываем класс-родитель, который делится методами
    def can_cure(self):
        print('Я могу лечить')

class Architect1(Person):  # подкласс, в скобках прописываем класс-родитель, который делится методами
    def can_build(self):
        print('Я могу строить здания')

''' Как проверить "родственность" классов '''

print(issubclass(Doctor1, Person))  # --> True Doctor1 наследник родителя Person

''' Цепочки могут быть разной длины? ниже создадим класс, который наследует от Doctor1, который
    в свою очередь наследует от Person и таким образом мы подадим ему 2 метода в наследство, при этом не
    прописав ни одного своего '''

class Ortoped(Doctor1):
    pass