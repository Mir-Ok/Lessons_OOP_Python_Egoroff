class Addition:

    def __init__(self):
        self.summa = 0

    def __call__(self, *args):
        for i in args:
            if isinstance(i, (int, float)):
                self.summa += i
        print(f'Сумма переданных значений = {self.summa}')
        self.summa = 0


#  --- Вариант 2

class Addition:
    def __call__(self, *args):
        print(f"Сумма переданных значений = {sum([i for i in args if isinstance(i,(int,float))])}")

#  --- Вариант 3


class Addition:
    def __call__(self, *args, **kwargs):
        result = sum(filter(lambda x: isinstance(x, (int, float)), args))
        print(f"Сумма переданных значений = {result}")



add = Addition()

add(10, 20) # печатает "Сумма переданных значений = 30"
add(1, 2, 3.4) # печатает "Сумма переданных значений = 6.4"
add(1, 2, 'hello', [1, 2], 3) # печатает "Сумма переданных значений = 6"


''' Реализация метода __call__ нужна, когда мы хотим, чтобы экземпляры класса вели себя как функции.
    А поскольку метод __call__ делает экземпляр вызываемым, 
    мы можем использовать его в качестве декоратора  '''

class Storage:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Подключение к хранилищу")
        self.func()
        print("Отключение от хранилища")

@Storage
def upload_file():
    print("Загрузка файла....")

upload_file()