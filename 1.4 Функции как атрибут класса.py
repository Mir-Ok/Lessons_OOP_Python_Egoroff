# внутри класса можно объявлять не только переменные, но и функции (они станут методом класса)

class Car:
    model = 'BMW'
    engine = 1.6

    def drive():  # при создании автоматически создается параметр self, пока удалим, далее изучим подробнее
        print('Let"s go')

print(Car.__dict__)

''' Результат 
    {'__module__': '__main__', 'model': 'BMW', 'engine': 1.6, 
    'drive': <function Car.drive at 0x0000022E1DB3B5E0>, 
    '__dict__': <attribute '__dict__' of 'Car' objects>, 
    '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
    
    Видим функцию в словаре класса
    '''

# Вызовем метод функции
print(Car.drive())  # --> Let"s go None

# Вызов функции через функцию getattr, не забываем ()
print(getattr(Car,'drive')())  # --> Let"s go None

# Снова смотрим, что при создании экземпляра, в его пространстве имен все пусто, исходные функи так же
# живут в пространстве имен исходного класса

a = Car()
print(a.__dict__)  # --> {}

print(a.drive) # --> <bound method Car.drive of <__main__.Car object at 0x000001A205907400>>
               # то, что для класса функция - стало методом для ее переменной,
               # поэтому вызвать функцию через экземпляр НЕЛЬЗЯ

''' Для класса это функция, для экземпляра класса - это метод! 
    То есть Car.drive() сработает, а a.drive() выдаст ошибку. 
    Во втором случае надо как метод a.drive, без скобок'''

''' Чтобы сделать функцию доступной от экземпляра, и от класса одновременно,
    используем декоратор @staticmethod
    '''

class Car:
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def drive():  # при создании автоматически создается параметр self, пока удалим, далее изучим подробнее
        print('Let"s go')

print(Car.drive())  # --> Let"s go None
print(a.drive())    # --> Let"s go None