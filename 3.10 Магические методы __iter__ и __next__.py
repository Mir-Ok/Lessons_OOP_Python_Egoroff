''' Важные! Делают экземпляры итерируемыми и доступными для прохода в цикле
    Магические методы __iter__ и __next__ '''


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks


igor = Student('Igor', 'Nikolaev', [3, 5, 5, 4, 3])

# for i in igor:
#     print(i)  # --> TypeError: 'Student' object is not iterable

# Как работают итераторы?
a = [1, 2, 3]
b = iter(a)
print(next(b))  # --> 1
print(next(b))  # --> 2
print(next(b))  # --> 3
# print(next(b))  # --> StopIteration потому что элементы закончились, обход один раз

# чтобы пройти второй раз, нужно создать новый итератор, воспользуемся в этот раз магическим методом
c = a.__iter__()
print(next(c))  # --> 1
print(c.__next__())  # --> 2 обращение через магический метод вместо функции дает аналогичный результат

''' Важно, что когда мы через цикл for  проходми коллекцию, под капотом Питон
    вызывает функцию iter() и к ней вызывает функцию next(). Когда элементы заканчиваются,
    мы не получаем ошибку, просто перебор заканчивается, исключание обрабатывается само '''

''' Какие есть возможности сделать экземпляр класса итерируемым?
    
    Вариант 1. При помощи метода __getitem__ обратится к элементу по индексу '''

class Student2:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

igor2 = Student2('Igor', 'Nikolaev', [3, 5, 5, 4, 3])

for i in igor2:
    print(i)  # --> TypeError: 'Student' object is not iterable
''' I
    g
    o
    r
    
    поочередный вывод символов строки '''

''' Вариант 2.
    Метод __iter__ '''

class Student3:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print('Iter called')
        return iter(self.surname)  # возвращаем функцию-итератор

    # сейчас у нас две функции, и при итерации Питон руководствуется __iter__, на
    # __getitem__ не посмотрит, так как он в первую очередь отвечает за обращение по индексу

igor3 = Student3('Igor', 'Nikolaev', [3, 5, 5, 4, 3])

for i in igor3:
    print(i)  # --> TypeError: 'Student' object is not iterable

    ''' Iter called
        N
        i
        k
        o
        l
        a
        e
        v
        
        Обратился именно к фамилии
        
        Все хорошо срабатывает, потому что идет обращение к строке (это встроенный класс str), 
        а он по умолчанию знает, как итерироваться.
        Если мы сделаем обращение внутри нашего метода, то есть вместо return iter(self.surname) 
        пропишем return self - то мы получим ошибку
        
        Как исправить, как научить обходить именно объект класса Student()?  
        '''

class Student4:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print('Iter called')
        self.index = 0
        return self # возвращаем объект класса

    # прописываем отдельно логику обхода элементов объекта класса
    # описываем поочередное возвращение
    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

''' В классе выше организован обход по имени. 
    Учитывается его длина, обработаны исключения
    Учтена первая буква и добавлен счетчик для перебора начиная со второй '''

''' Для перебора оценок создадим отдельный класс, чтобы не вносить путаницу '''

class Marks:
    def __init__(self, marks):
        self.marks = marks
        self.index = 0

    def __iter__(self):
        return self  # возвращаем Marks()

    def __next__(self):
        print('Called __next__ Marks()')
        if self.index >= len(self.marks):
            self.index = 0  # добавляем обнуление счетчика при исключении
            raise StopIteration
        letter = self.marks[self.index]
        self.index += 1
        return letter


class Student5:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print('Iter called')
        self.index = 0
        return iter(self.marks)  # возвращаем объект класса

    def __next__(self):
        print('Called __next__ Student4()')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


m = Marks([3, 5, 5, 4, 3])

igor5 = Student5('Igor', 'Nikolaev', m)  # подаем экземпляр класса в исходный класс

for i in igor5:
    print(i)

''' Iter called
    Called __next__ Marks()
    3
    Called __next__ Marks()
    5
    Called __next__ Marks()
    5
    Called __next__ Marks()
    4
    Called __next__ Marks()
    3
    Called __next__ Marks()
    
    '''

'''' Кусок теории 

Бесконечный итератор
Иногда мы хотим, чтобы наш итератор продолжал работать, пока не будет выполнено определенное условие. Но если мы неправильно определим условие, то столкнемся с бесконечным итератором, который никогда не закончится. Следовательно, при работе с такими итераторами необходимо проявлять особую осторожность.

Давайте разберем такой итератор, и поможет нам вновь встроенная функция iter.

help(iter)
Help on built-in function iter in module builtins:
iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator
    
    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
Документация говорит, что функция iter может быть вызвана от двух аргументов:

callable - вызываемый объект
sentinel - значение, обозначающее конец последовательности
Функция iter будет каждый раз вызывать объект callable и сравнивает его со вторым аргумент sentinel. Как только они совпадут, будет исключение StopIteration

В качестве вызываемого объекта мы можем выбрать выражение int()

int() # возвращает 0
Используем это выражение в итераторе

>>> int()
0
>>> inf_iter = iter(int, 999)
>>> next(inf_iter)
0
>>> next(inf_iter)
0
При каждом вызове next будет вызываться int(), который постоянно возвращает 0, а 0 никогда не равен значению 999. Отсюда получаем бесконечный итератор.

Но если в качестве второго аргумента передадим 0, то сразу получим StopIteration, так как значения совпадут

>>> not_inf = iter(int, 0)
>>> next(not_inf)
Traceback (most recent call last):
  File "C:\Python3.9\lib\site-packages\IPython\core\interactiveshell.py", line 3457, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-17-3ca409f2299a>", line 1, in <module>
    next(not_inf)
StopIteration

    '''