''' Магический метод __call__
    Это вызов, оператор, который вызывается двумя скобками ()

    Если мы создаем класс, то он вызываемый. Результат вызова - создание нового экземпляра класса '''

class Counter:

    def __init__(self):
        print('init object', self)

''' Создание трех объектов в консоли при вызове Counter, как видим все они разные:

    Counter()
    init object <__main__.Counter object at 0x000001A63BBE27F0>
    Out[3]: <__main__.Counter at 0x1a63bbe27f0>
    
    Counter()
    init object <__main__.Counter object at 0x000001A63BBE2CD0>
    Out[4]: <__main__.Counter at 0x1a63bbe2cd0>
    
    Counter()
    init object <__main__.Counter object at 0x000001A63BBE2490>
    Out[5]: <__main__.Counter at 0x1a63bbe2490>
    
    '''

class Counter2:

    def __init__(self):
        print('init object', self)

    def __call__(self, *args, **kwargs):
        print(f' Объект {self} вызывался')

a = Counter2()
print(a)  # --> init object <__main__.Counter2 object at 0x0000026CAC207DF0>
print(a())  # --> Объект <__main__.Counter2 object at 0x0000026CAC207DF0> вызывался



class Counter3:

    def __init__(self):
        # создадим счетчик при создании класса
        self.counter = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f' Объект {self} вызывался {self.counter} раз')

a = Counter3()
a()  # --> Объект <__main__.Counter3 object at 0x000001EDDDBF7EB0> вызывался 1 раз
a()  # --> Объект <__main__.Counter3 object at 0x000001EDDDBF7EB0> вызывался 2 раз
a()  # --> Объект <__main__.Counter3 object at 0x000001EDDDBF7EB0> вызывался 3 раз
a()  # --> Объект <__main__.Counter3 object at 0x000001EDDDBF7EB0> вызывался 4 раз


''' В теме про замыкания мы рассматривали функцию, что принимает аргументы и находит их среднне
    арифметическое.
    Воссоздадим подобный класс, который принимает порциями аргументы, считает их, суммирует и
    находит среднее арифметическое '''


class Counter4:

    def __init__(self):
        # создадим счетчик при создании класса
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f' Объект {self} вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length



q = Counter4()
q(3, 4, 5)
print(q.summa)
print(q.length)

q(3, 4, 8)
print(q.summa)
print(q.length)

q(8)
print(q.summa)  # без скобок, это свойство
print(q.length)
print(q.average())  # со скобками, это метод

# Все верно, всего 7 элементов с суммой 35



''' Пришло время реализовать замыкания и декоратор '''

from time import perf_counter

class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывалась функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result

# факториал
def fuct(n):

    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr

# рекурсивный Фибоначчи
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

''' Начинаем декорирование, но сначала с базового варианта 
    Сохраним ее название и переопределим, теперь в fib хранится 
    экземпляр класса Timer(который принимает функция в аргумент), 
    а не функция '''

fuct = Timer(fuct)
fuct(5)  # Вызывалась функция fuct
         # Функция отработала за 9.399999999999686e-06

fib = Timer(fib)
fib(5)  # все хорошо, но выводятся наши рекурсивные вызовы, т.е fib(20)
        # вызовет fib(19) и fib(18), они в свою очередь вызовут по две функции
        # fib(18),fib(17) и fib(17),fib(16) ... и в иоге мы не видим конечный результат,
        # только отработки каждой вложенной функции

''' Решение - задекорировать не всю функцию целиком, а только ее вызов '''
Timer(fib)(7)   # корректно отрабатывает
                # Вызывалась функция fib
                # Функция отработала за 0.0001021999996737577
                # Out[15]: 13


# Причем обычный вызов функции сработает стандартно, т.к. она не декорирована полностью
fib(6)

