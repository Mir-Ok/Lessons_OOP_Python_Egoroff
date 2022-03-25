class Bankaccount:

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


''' Создадим объект класса property() и вызовем его '''

x = property()
print(x)  # --> <property object at 0x00000151AD176CC0>

# посмотрим через точку список доступных для х методов, среди них будут getter(), setter(), deleter()
print(x.getter(90))  # --> <property object at 0x000001606E956AE0>

''' Запись выше показывает, что мы можем передавать в методы что-то. Например, наши функции.
    Перепишем класс '''

class Bankaccount1:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    def get_balance(self):
        print('Сработал метод get_balance')
        return self.__balance

    def del_balance(self):
        print('Сработал метод del_balance')
        del self.__balance

    # set - уcтанавливать значения
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            print('Сработал метод set_balance')
            self.__balance = value

    # запишем в развернутом виде
    # my_balance = property()
    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(del_balance)

    # Оптимизируем запись выше
    my_balance = property(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(del_balance)

# создадим пользователя
a = Bankaccount1('Иван', 100)
print(a.my_balance)  # --> Сработал метод get_balance   100

''' На данный момент у нас образовалась двойная функциональность.
    Мы можем обращаться к методам и напрямую, и через свойства. 
    Используем запись через декораторы  '''

class Bankaccount1:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # эта функция стала методом, так как она под декоратором
    @property
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance

    @my_balance.deleter
    def my_balance(self):
        print('Сработал метод del_balance')
        del self.__balance
    #
    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            print('Сработал метод set_balance')
            self.__balance = value

