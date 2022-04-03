''' Как мы можем создавать свои?

    Вспоминая иерархи, наследуемся от Exception.
    Потому что если взять то, что на одном уровне - ошибки будут проскакивать
    Иерархия строгая '''


class MyExcertion(Exception):
    """ this is my first Exception """


# raise MyExcertion
''' вывод

    Traceback (most recent call last):
      File "D:/1_Python/ООП на Python (Egoroff)/5.5 Пользовательские исключения в Python.py", line 8, in <module>
        raise MyExcertion
    __main__.MyExcertion
    
    '''

# можем передавать аргументы и они сохранятся в кортеж
# raise MyExcertion('hello', 1, 2, 3)
''' вывод

    Traceback (most recent call last):
      File "D:/1_Python/ООП на Python (Egoroff)/5.5 Пользовательские исключения в Python.py", line 8, in <module>
    raise MyExcertion('hello',1,2,3)
    __main__.MyExcertion: ('hello', 1, 2, 3)

    '''

# обработаем исключение
try:
    raise MyExcertion('hello', 1, 2, 3)
except MyExcertion:  # указываем тип исключения, который здесь обработается
    print('done')

    ''' вывод
    
    done 
    
    '''

# мы можем переопределять методы класса исключений
class MyExcertion(Exception):
    """ this is my first Exception """

    def ___init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('str called')
        if self.message:
            return f'MyException ({self.message})'
        else:
            return f'MyException is Empty'


''' Мы можем выстраивать иерархию своих исключений '''

class SnakeBaseException(Exception):  # наследуем встроенному классу ошибок
    """ основной класс ошибок змейки"""

class SnakeBorderException(SnakeBaseException):  # наследуем нашему классу
    """ ошибка соприкосновения со стенкой """

class SnakeTailException(SnakeBaseException):  # наследуем нашему классу
    """ касание головы и хвоста """