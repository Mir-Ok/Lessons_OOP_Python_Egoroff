class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)

account1 = BankAccount('Bob', 100000, 45474845)

''' Разделим программу на две части. 
    То, что внутри класса. Чтобы банк мог осуществлять деятельность, он должен иметь доступ к данным (атрибутам)
    своих клиентов.  
    
    На данный момент вообще никаких защит нет, убедимся, вызвав метод .print_data(), а
    также вызвав атрибуты по отдельности 
     '''

account1.print_public_data()  # --> Bob 100000 45474845, доступен в рамках банка
print(account1.name)   # --> Bob, просто доступен вне рамок банка, и это НЕ безопасно

''' Наша задача сделать так, чтобы атрибуты были доступны внутри банка и НЕ доступны вне рамок банка '''


''' Protected 
    Переменные дополняются _ и name становится _name '''

class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

account1 = BankAccount('Bob', 100000, 45474845)

account1.print_protected_data()  # --> Bob 100000 45474845
print(account1._name)            # --> 10000

# Доступ сохранился, все еще не безопасно. Это уровень согласования между разработчиками,
# то есть сам язык дает возможность обращаться, но это вам знак от разраба, точ его лучше не трогать,
# он для работы внутри класса

''' Privats '''

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 100000, 45474845)

account1.print_private_data()    # --> Bob 100000 45474845
print(account1.__name)           # --> AttributeError: 'BankAccouunt' object has no attribute '__name'

''' Обращаем внимание, что доступ к атрибутам внутри класса через метод все еще есть, даже с __ 
    Сокрытие обработки защищенных атрибутов - это ИНКАПСУЛЯЦИЯ. То есть мы сохраняем 
    возможность работать даже с самыми защищенными данными - метод .print_private_data().
    Сами даннные напрямую закрыты.
    
    Аналогично можно защитить и метод '''

class BankAccouunt:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    # def print_private_data(self):
    #     print(self.__name, self.__balance, self.__passport)

    # хитрость, как обойти закрытый метод? помещаем его в открытый
    def print_public_data(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Bob', 100000, 45474845)

account1.__print_private_data()    # --> AttributeError:
print(account1.__name)             # --> AttributeError: 'BankAccouunt' object has no attribute '_name'

print(account1.print_public_data())  # --> Bob 100000 45474845

''' Какие есть еще варианты? '''

account1 = BankAccouunt('Bob', 100000, 45474845)
# вызовем список атрибутов через dir()
print(dir(account1))  # -->  ['_BankAccouunt__balance', '_BankAccouunt__name',  ... ]

print(account1._BankAccouunt__balance)  # --> 10000 Подсмотрели название метода и обратились через него

''' Чтобы полностью защитить - модуль accesify '''