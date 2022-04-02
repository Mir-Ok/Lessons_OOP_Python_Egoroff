''' Множественое наследование - это возможность наследовать нескольким родителям

    Порядок перечисления важен '''


class Builder():

    def can_build(self):  # доступно и этому классу, и потомку
        print('Строитель умеет строить')


class Doctor():

    def can_cure(self):  # доступно и этому классу, и потомку
        print('Доктор умеет лечить')


class Person(Doctor, Builder):
    pass


p = Person()
p.can_cure()  # -->  Доктор умеет лечить
p.can_build()  # -->  Строитель умеет строить

''' Смоделируем ситуацию с наследованием имен '''


class Builder1:

    def can_build(self):  # доступно и этому классу, и потомку
        print('Строитель умеет строить')


class Doctor1:

    def can_cure(self):  # доступно и этому классу, и потомку
        print('Доктор умеет лечить')


class Person1(Doctor1, Builder1):

    def can_build(self):
        print('Я человек, я тоже умею строить ')


p1 = Person1()
p1.can_cure()  # -->  Доктор умеет лечить
p1.can_build()  # -->  Я человек, я тоже умею строить - отработал только "свой" метод,
# обычное наследование


''' Смоделируем ситуацию с наследованием имен '''


class Builder2:

    def can_build(self):  # доступно и этому классу, и потомку
        print('Строитель умеет строить')


class Doctor2:

    def can_cure(self):  # доступно и этому классу, и потомку
        print('Доктор умеет лечить')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень ')


class Person2(Doctor2, Builder2):
    pass


p2 = Person2()
p2.can_build()  # -->  Я доктор, я тоже умею строить, но не очень
# берем у первого родителя, класса Доктор, если найдется - отработает
# смена порядка родителей изменит ситуацию

print(Person2.__mro__)  # где mro - method fesolution object - порядок в котором перебираем классы при помощи
# (<class '__main__.Person2'>, <class '__main__.Doctor2'>, <class '__main__.Builder2'>, <class 'object'>)

''' Прикрутим делегирование '''


class Builder3:

    def graduate(self):
        print('Ура, я отучился на строителя')

    def can_build(self):  # доступно и этому классу, и потомку
        print('Строитель умеет строить')


class Doctor3:

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_cure(self):  # доступно и этому классу, и потомку
        print('Доктор умеет лечить')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень ')


class Person3(Doctor3, Builder3):

    def graduate(self):
        print('Посмотрим, кем я стал')
        super().graduate()


p3 = Person3()
p3.graduate()  # Посмотрим, кем я стал   Ура, я отучился на доктора
# Порядок снова по МРО, сначала у себя, потом у доктора, потом у строителя ...

''' Как вызвать метод у обоих родителей? 
    На примере только одного класса '''


class Person4(Doctor3, Builder3):

    def graduate(self):
        print('Посмотрим, кем я стал')
        super().graduate()
        Builder3.graduate(self)


p4 = Person4()
p4.graduate()  # Посмотрим, кем я стал   Ура, я отучился на доктора   Ура, я отучился на строителя

''' Рассмотрим ситуацию сложнее, когда каждый метод должен принимать свои аргументы '''


class Doctor5:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_cure(self):  # доступно и этому классу, и потомку
        print('Доктор умеет лечить')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень ')


class Builder5:

    def __init__(self, rang):
        self.rang = rang

    def graduate(self):
        print('Ура, я отучился на строителя')

    def can_build(self):  # доступно и этому классу, и потомку
        print('Строитель умеет строить')


class Person5(Doctor5, Builder5):

    def __init__(self, degree, rang):
        self.degree = degree
        self.rang = rang

    def __str__(self):
        return f'Ранг {self.rang} и степень {self.degree}'

p5 = Person5(5, 'doc')
print(p5)  # --> Ранг doc и степень 5

''' Если мы прикрутим делегирование, то нам придется обратиться к каждому из классов-
    родителей отдельно и подать аргумент '''

class Person5(Doctor5, Builder5):

    def __init__(self, degree, rang):
        super().__init__(degree)  # так как первый по порядку родитель Доктор, без self
        Builder5.__init__(self, rang)  # прямое обращение ко второму родителю

    def __str__(self):
        return f'Ранг {self.rang} и степень {self.degree}'
