''' Для чего нужны вообще эти свойства и декораторы?

    Какая самая большая проблема класса? В том, что к его атрибутам можно обращаться, даже менять
    и реализация класса этому никак не мешает.

    Проблема в том, что мы должны во-первых ограничить доступ к информации, во-вторых добавить
    условия к паролю (строка с цифрой, интервал длины, не из банальных  и пр.)

    При помощи property мы можем отловить момент обращения к паролю, или попытку его изменения
    (геттер и сеттер соотв) и в момент отлова можем на него повлиять '''

from string import digits  # набор цифр в виде строки '0123456789'

class User:

    # проверка значения на наличие цифр, сделаем ее статическим методом, то есть при вызове в нее
    # не подается ни класс, ни экземпляр, только проверяемое выражение, хотя функция лежит внутри класса
    @staticmethod
    def is_include_number(password):  # нет self благодаря @staticmethod
        for digit in digits:  # переберем '0123456789'
            if digit in password:
                return True  # если хоть одна цифра, то да и завершится
        return False  # если не одной цифры не найдется, то вернет нет

    def __init__(self, login, password):
        self.login = login
        self.my_password = password  # self.my_password вместо self.__password, заменили имя атрибута названием свойства,
                                     # чтобы при первом же вводе пароля сразу запустить проверку

    @property
    def my_password(self):
        print('getter called')

        # возвращаем защищенный атрибут нашего экземпляра
        return self.__password

    # создаем сеттер, который прежде чем устанавливать пароль, прогонит его через условия
    @my_password.setter
    def my_password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Длина пароля не менее 4 символов')
        if len(value) > 12:
            raise ValueError('Длина пароля не более 12 символов')
        if not User.is_include_number(value):  # обратимся к функции через класс
            # если цифры нет, то вернется исключение
            raise ValueError('пароль должен состоять как минимум из одной цифры')

        self.__password = value

    # вывод секретного параметра при вводе пароля
    @property
    def secret(self):
        s = input('Введите пароль: ')
        if s == self.password:  # обратимся к паролю через свойство
            return
        else:
            raise ValueError('Неверный пароль!')

''' На данный момент проверка пароля производится только при замене, исходный при создании
    экземпляра класса не проверяется 
    
    Поэтому мы в конструкторе убираем __ перед password и тут же задание пароля начнет 
    обрабатываться setter-ом'''

# p = User('abc', 123)  # TypeError: Пароль должен быть строкой   setter called

p = User('abc', 'fgfg123')  # сработало, пароль установлен
print(p.__dict__)








