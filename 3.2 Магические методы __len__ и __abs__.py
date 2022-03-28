''' Магические методы, лответственные за выполнение математических операций

    __add__, __mul__, __sub__, __truediv__ '''


class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


b = Bankaccount('Ivan', 900)
