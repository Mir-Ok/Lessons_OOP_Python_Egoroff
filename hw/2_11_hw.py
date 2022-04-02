''' Давайте создадим класс Registration, который поможет зарегистрировать пользователя с безопасным паролем '''
from string import digits  # набор цифр в виде строки '0123456789'
import string

with open('easy_passwords.txt') as f:
    my_set = list(f)

class Registration:

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    # проверка на содержание цифр
    @staticmethod
    def is_include_number(password):
        for digit in digits:  # переберем '0123456789'
            if digit in password:
                return True  # если хоть одна цифра, то да и завершится
        return False  # если не одной цифры не найдется, то вернет нет

    # проверка, что все латинница в обоих регистрах
    @staticmethod
    def is_include_only_latin(password):
        for digit in string.ascii_letters:  # переберем 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if digit in password:
                return True
        return False

    # проверка, что есть как минимум два в верхнем
    @staticmethod
    def is_include_all_register(password):
        i = 0
        for pswrd in password:  # переберем 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if pswrd in string.ascii_uppercase:
                i += 1
        if i > 1 and i < len(password) - 2:
            return True
        else:
            return False

    # создание геттера
    @property
    def password(self):
        return self.__password

    # создаем сеттер, который прежде чем устанавливать пароль, прогонит его через условия
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 5 and len(value) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_number(value):  # обратимся к функции через класс
            # если цифры нет, то вернется исключение
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if value in my_set:
            raise ValueError('Ваш пароль содержится в списке самых легких')

        self.__password = value

    # создание геттера
    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, n_login):
        if  n_login.count("@")<1:
            raise ValueError("Login must include at least one ' @ '")
        if not "." in n_login:
            raise ValueError("Login must include at least one ' . '")

        self.__login = n_login

s2 = Registration("fga", "asd12")
print(s2.__dict__)
