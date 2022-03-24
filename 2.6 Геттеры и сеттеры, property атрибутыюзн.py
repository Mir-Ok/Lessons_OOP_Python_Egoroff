class Bankaccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

''' Проблема: у метода инициализации есть два атрибута, они оба публичные, к ним можно обратиться вне класса/
    Это значит, что мы можем обратиться в ним и даже изменить вне класса. Небезопасно.
    '''

a = Bankaccount('Ivan', 100)
print(a.balance)  # --> 100
print(a.name)     # --> Ivan

''' Сделаем атрибут balance приватным и предоставим интерфейс, при помощи которого будем получать 
    и устанавливать значения '''

class Bankaccount1:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    def get_balance(self):
        return self.__balance

    # set - уcтанавливать значения
    def set_balance(self, value):
        self.__balance = value

b = Bankaccount1('Вася', 150)
# b.__balance  # --> AttributeError: 'Bankaccount1' object has no attribute '__balance'
b.get_balance()  # --> 100
b.set_balance(250)
print(b.__dict__)  # -->  {'name': 'Вася', '_Bankaccount1__balance': 250}

''' Стало лучше, но все равно нет защиты от того, что я метод set_balance() может быть передана строка вместо числа, 
    например  '''

class Bankaccount2:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    def get_balance(self):
        return self.__balance

    # set - уcтанавливать значения
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            self.__balance = value

d = Bankaccount2('Инна', 241)
# d.set_balance('text')  # --> ValueError: Не число
d.set_balance(288)
print(d.__dict__)  # --> {'name': 'Инна', '_Bankaccount2__balance': 288}


''' Стало лучше, но теперь есть неудочбство с заданием инкапсулированных аргументов, нужно вызывать функции.
    Простым оператором присваивания уже не сделать '''

class Bankaccount3:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    def get_balance(self):
        return self.__balance

    def del_balance(self):
        del self.__balance

    # set - уcтанавливать значения
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            self.__balance = value

    # создаем имя нашего свойства
    balance = property(fset=set_balance, fget=get_balance, fdel=del_balance)

e = Bankaccount3('Миша', 400)
print(e.balance)  # --> 400
e.balance = 250
print(e.balance)  # --> 250  мы снова получили возможность его изменять