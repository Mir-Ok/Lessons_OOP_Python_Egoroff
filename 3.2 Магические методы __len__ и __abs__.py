''' Магические методы, лответственные за выполнение математических операций

    __add__, __mul__, __sub__, __truediv__ '''


class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


b = Bankaccount('Ivan', 900)

print(b.balance + 250)  # --> 1150 можем суммировать числа

# print(b + 250)  # --> TypeError: unsupported operand type(s) for +: 'Bankaccount' and 'int'

''' Чтобы добаить возможность сложения с экземплыром класса, 
    точнее с одним из его определенных атрибутов '''

class Bankaccount2:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')
        # проверяем, что подаваемое значение является числом
        if isinstance(other, (int, float)):
            # если да, то суммируем с балансом
            return self.balance + other

c = Bankaccount2('Misha', 900)
print(c + 450)  # --> __add__ called   1350 прямое суммирование с экземпляром заработало

''' Добавим возможность суммирования средств двух клиентов банка '''

class Bankaccount3:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')
        # проверяем, что подаваемое значение является экземпляром этого же класса'
        if isinstance(other, Bankaccount3):
            return self.balance + other.balance
        # проверяем, что подаваемое значение является числом
        if isinstance(other, (int, float)):
            # если да, то суммируем с балансом
            return self.balance + other
        # в иных случаях ошибка
        raise NotImplemented

d = Bankaccount3('Misha', 900)
e = Bankaccount3('Tanya', 900)
print(d+e)  # --> __add__ called   1800 прямое суммирование с экземпляроВ заработало

''' Есть еще олна проблема 
    c + 450 прекрасно срабатывает, а 450 + с вызывает ошибку, т.к. Питон у первого объекта вызывает метод __add__
    '''

class Bankaccount4:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')
        # проверяем, что подаваемое значение является экземпляром этого же класса'
        if isinstance(other, Bankaccount3):
            return self.balance + other.balance
        # проверяем, что подаваемое значение является числом
        if isinstance(other, (int, float)):
            # если да, то суммируем с балансом
            return self.balance + other
        # в иных случаях ошибка
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ called')
        return self+other

d = Bankaccount4('Misha', 900)
print(d+15)  # --> __add__  called   915
print(15+d)  # --> __radd__ called   __add__ called   915 даже с перестановкой сработало

''' C остальными методами, дли примера добавим умножение '''

class Bankaccount5:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')
        # проверяем, что подаваемое значение является экземпляром этого же класса'
        if isinstance(other, Bankaccount3):
            return self.balance + other.balance
        # проверяем, что подаваемое значение является числом
        if isinstance(other, (int, float)):
            # если да, то суммируем с балансом
            return self.balance + other
        # в иных случаях ошибка
        raise NotImplemented

    def __mul__(self, other):
        print('__mul__ called')
        # проверяем, что подаваемое значение является экземпляром этого же класса'
        if isinstance(other, Bankaccount3):
            return self.balance * other.balance
        # проверяем, что подаваемое значение является числом
        if isinstance(other, (int, float)):
            # если да, то суммируем с балансом
            return self.balance * other
        # если подаваемое строка, то конкатенируем
        if isinstance(other, (int, str)):
            return self.name + other
        # в иных случаях ошибка
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ called')
        return self+other

f = Bankaccount5('Misha', 900)
print(f*3)  # --> __mul__ called  2700
print(f*'rrr')  # --> __mul__ called  Misharrr

''' В методу __add__  выше мы возыращали число. А что если мы хотим вернуть объект, но уже
    с новым балансом '''

class Bankaccount6:

    def __init__(self, name, balance):
        print('new object init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):
        print('__add__ called')
        if isinstance(other, Bankaccount3):
            return self.balance + other.balance
        # если складываем с числом
        if isinstance(other, (int, float)):
            # вызываем наш класс, у которого сработает метод __init__ и изменим его
            return Bankaccount6(self.name, self.balance + other)
        # в иных случаях ошибка
        raise NotImplemented

h = Bankaccount6('Ivan', 200)  # --> new object init
print(id(h))  # --> 1437890728144
print(h+30)  # --> отработает метод __add__ (__add__ called),
             # потом __init__(new object init) т.к. указан возврат нового аккаунта
             # итог работы -- > Клиент Ivan с балансом 230

''' Поместим вызов в новую переменную '''
m = h + 40  # __add__ called   new object init
print(m)  # --> Клиент Ivan с балансом 240
print(id(m))  # --> 1748526649648

''' Видим, что после изменения баланса это уже новая переменная, с другим id 

    В последнем классе мы получаем другое поведение, нежели ранее '''
