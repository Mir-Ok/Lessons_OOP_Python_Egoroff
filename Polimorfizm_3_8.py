''' Полиморфизм, до замены  '''

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_rect_area(self):
#         return self.a * self.b
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#     def get_square_area(self):
#         return self.a * self.a
#
# class Surcle:
#     def __init__(self, r):
#         self.r = r
#     def get_surcle_area(self):
#         return 3.14 * self.r ** 2

''' Полиморфизм, после замены  '''

# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_area(self):
#         return self.a * self.b
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#     def get_area(self):
#         return self.a * self.a
#
# class Surcle:
#     def __init__(self, r):
#         self.r = r
#     def get_area(self):
#         return 3.14 * self.r ** 2

''' Мы можем вызвать полиморфное поведение, определив метод
    __str__ '''

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a * self.b
    def __str__(self):
        return f'Rectangle sides = {self.a}, {self.b}'

class Square:
    def __init__(self, a):
        self.a = a
    def get_area(self):
        return self.a * self.a
    def __str__(self):
        return f'Square sides = {self.a}'


class Surcle:
    def __init__(self, r):
        self.r = r
    def get_area(self):
        return 3.14 * self.r ** 2
    def __str__(self):
        return f'Surcle radius = {self.r}'

''' 

Что такое полиморфизм?
Полиморфизм происходит от греческих слов poly (много) и morphism (формы), что в буквальном значении 
полиморфизм означает множество форм. Это означает, что одна и та же сущность (операция, функция, метод, объект) 
может использоваться для разных типов. Это делает программирование более интуитивным и простым.

В Python есть разные способы определения полиморфизма. Давайте посмотрим на эти варианты.

1. Полиморфизм в операциях
Мы знаем, что оператор + широко используется в программах Python. Но у него нет однозначного использования.

Для целочисленных типов данных оператор + используется для выполнения арифметической операции сложения.
Подобным образом оператор + для строк используется для конкатенации.
Один оператор + использовался для выполнения разных операций с разными типами данных. 
Это одно из самых простых проявлений полиморфизма в Python.

2. Полиморфные функции
В Python есть некоторые функции, которые могут принимать аргументы разных типов.

Одна из таких функций — len(). Она может принимать различные типы данных. Давайте посмотрим на примере, как это работает.

print(len("Fizz Buzz"))
print(len([1, 2, 3]))
print(len({"Name": "John", "Address": "UK"}))

Здесь мы можем увидеть, что различные типы данных, такие как строка, список, кортеж, множество и словарь 
могут работать с функцией len(). Однако, мы можем увидеть, что она 
возвращает специфичную для каждого типа данных информацию.

'''