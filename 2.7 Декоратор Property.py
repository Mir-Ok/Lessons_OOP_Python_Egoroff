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

    # запишем в развернутом виде, сначала создадим объект класса property() 
    # my_balance = property()
    
    # обратимся к его методам по умолчанию
    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(del_balance)

# создадим пользователя
a = Bankaccount1('Иван', 100)

print(a.my_balance)  # --> 100 Сработал метод get_balance, потому что мы запросили выдачу значения
print(a.my_balance = 500)   # --> 500 Сработал метод set_balance, потому что мы задали новое, а не вызвали

# Если оптимизируем запись выше и сразу подадим геттер - нчиего не изменится
#    my_balance = property(get_balance)
#    my_balance = my_balance.setter(set_balance)
#    my_balance = my_balance.deleter(del_balance)
    
    
''' На данный момент у нас образовалась двойная функциональность,
    мы можем обращаться к методам и напрямую get_balance(), и через свойства my_balance,  это не нужно
    
    Используем запись через декораторы. то есть уберем прямое обращение и оставим только через my_balance 
    Дальше используются декораторы, их надо изучить заранее отдельно 
    
    Оставим пока только часть кода, декорируем метод get_balance при помощи property()
    Меняем имя get_balance на my_balance и '''

class Bankaccount2:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance

    # def del_balance(self):
    # print('Сработал метод del_balance')
    # del self.__balance

    # def set_balance(self, value):
    #     if not isinstance(value, (int, float)):
    #         raise ValueError('Не число')
    #     else:
    #         print('Сработал метод set_balance')
    #         self.__balance = value

    my_balance = property(get_balance)  
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(del_balance)

b = Bankaccount2('Миша', 120)
print(b.my_balance)  # --> get balance 120 
                     #     Важно, вызываем как свойство, без (), потому что они вызовут ошибку not callable
                     #     Метод стал свойством из-за декорирования

''' Раз у нас есть декоратор, мы можем воспользоваться синтаксическим сахаром '''

class Bankaccount3:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    @property
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance

    # my_balance = property(get_balance)  - переехало наверх в виде @property

# проверим, увидим аналогичную работу
b = Bankaccount2('Саша', 180)
print(b.my_balance)  # --> get balance 180     
    
''' Займемся добавлением set_balance() 

    Раз my_balance() стало объектом класса свойств, то у него есть метод .setter'''    

class Bankaccount4:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    @property
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance
    
    # вернем метод
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            print('Сработал метод set_balance')
            self.__balance = value
    
    my_balance = my_balance.setter(set_balance)  # аргумент именно set_balance
 
''' При проверке все сработает, кроме того, что у нас снова наложение: доступны и через свойство set_balance, и через метод set_balance()
    Чтобы метод стал свойством, нужно его назвать так же, как и декоратор, но тогда у нас возникнет конфликт имен, будет два my_balance()
    Новосозданная функция затрет задекорированный выше метод, это портит функциональность.
    
    Чтобы этого избежать создается переменная, в которой лежит метод: '''

class Bankaccount4:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    # get - предоставлять
    @property
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance
    
    # как раз таки добавленная переменная для сохранения метода
    my_property_balance = my_balance
    
    # вернем метод
    def my_balance(self, value):  # вот она новая функция, которая могла из-за сходства названий затереть метод my_balance
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            print('Сработал метод set_balance')
            self.__balance = value
    
    my_balance = my_property_balance.setter(set_balance)  # через сохраненное свойство вызываем метод setter и ему передаем функцию set_balance
    # благодаря этой махинации, my_balance опять становится свойством
    
''' Мы вернулись к тому, что у нас снова есть метод my_balance, но нет функции 
    Записанное выше можно упростить, так как у свойства my_balance есть метод setter '''
 
class Bankaccount5:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance
    
    # как раз таки добавленная переменная для сохранения метода? больше не нужна
    # my_property_balance = my_balance
    
    @my_balance.setter
    def my_balance(self, value):  # вот она новая функция, которая могла из-за сходства названий затереть метод my_balance
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            print('Сработал метод set_balance')
            self.__balance = value
    
    # my_balance = my_property_balance.setter(set_balance) - больше не нужна
    
''' Переопределим класс и увидим, что все методы у нас пропали, осталось только свойство my_balance, с которым мы работаем, как с атрибутом класса, по сути, 
    в не как с методом
    Можем вызывать текущее значение или вызывать новое, и еще можем добавить deleter '''
    
class Bankaccount5:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('Сработал метод get_balance')
        return self.__balance
    
    @my_balance.setter
    def my_balance(self, value):  # вот она новая функция, которая могла из-за сходства названий затереть метод my_balance
        if not isinstance(value, (int, float)):
            raise ValueError('Не число')
        else:
            print('Сработал метод set_balance')
            self.__balance = value    
    
    @my_balance.deleter  # вешаем декоратор с нужным методом
    def my_balance(self):  # меняем del_balance на my_balance
        print('Сработал метод del_balance')
        del self.__balance    
    
''' Самое важно, что надо знать при работе со свойствами 

    Геттеры и сеттеры мы должны называть одинаково
    Если вдруг будут разные имена, то обращаться к значению баланса (balance) мы сможем, а установить - уже нет, если забудем поменять название функции set_balance() 
    на my_balance(), потому что у нас не будет такого свойства как установка. 
    Это свойство доступно по имени set_balance, не по my_balance 
    
    Причем set_balance при неизмененном  имени будет работать и как сеттер, и как геттер
    И my_balance работает, но как геттер, как сететр не может, ошибка 
    Чтобы избежать такой двойной, но обрезанной функциональности - называем геттери и сеттеры одним именем '''

