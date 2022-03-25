class Example:

    def hello():
        print('hello')

# Обратимся к функции ОТ КЛАССА без вызова и получим ссылку на функцию
print(Example.hello)  # --> <function Example.hello at 0x000001FA509EDC10>

# Обратимся к функции ОТ КЛАССА с вызовом и получим результат ее работы
print(Example.hello())  # --> hello

# создадим экземпляр класса
p = Example()

# Обратимся к функции ОТ ЭКЗЕМПЛЯРА без вызова и получим ссылку на метод
print(p.hello)  # --> <bound method Example.hello of <__main__.Example object at 0x000001F959E08400>>

# Обратимся к функции ОТ ЭКЗЕМПЛЯРА с вызовом и получим ошибку
# print(p.hello())  # --> TypeError: hello() takes 0 positional arguments but 1 was given

''' Ошибка произошла потому что при вызове от экземпляра в функцию подается сам экземеляр
    (для него мы резервируем в скобках self), но его здесь нет и поэтому ошибка 
    
    То есть функция, созданная внутри класса может быть вызвана от класса, 
    но не может быть вызвана от экземпляра
    
    Чтобы вызывать от экземпляра, мы создаем методы, т.е. функции с обязательным аргументом self '''

# Изменим класс, добавим метод и в нем будем вызывать подаваемый в него аргумент

class Example1:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

q = Example1()
print(q.instance_hello())  # --> instance_hello <__main__.Example1 object at 0x000001FEA648A280>
print(q)  # --> <__main__.Example1 object at 0x000002730FFFA280>
''' Теперь мы можем вызывать функцию (точнее метод) от экземпляра
    Обратим внимание, что адреса q вызванного отдельно и вывееднного через метод совпадают 
    
    Но появилась другая проблема, от класса уже не удается вызвать instance_hello() 
    Это происходит потому что функция не привязана к классу и нет автоматического помещения класса в аргумент self
    
    '''

# Example1.instance_hello()  # --> TypeError: instance_hello() missing 1 required positional argument: 'self'
                           # ругается, что не подан ожидаемый аргумент

''' Суть проблемы:
    - функцию hello() мы можем вызвать от класса, но НЕ может от экземпляра
    - функцию instance_hello() мы НЕ можем вызвать от класса, но можем от экземпляра 
    
    Как создать внутри класса функцию, которая будет вызываться и от класса, и от экземпляра? 
    
    При помощи @staticmethod '''

class Example2:

    def hello():
        print('hello')

    @staticmethod
    def static_hello():  # БЕЗ self
        print('static_hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

# Обратимся к функции ОТ КЛАССА с вызовом и получим результат ее работы
print(Example2.static_hello())  # --> static_hello

y = Example2()
# Обратимся к функции ОТ ЭКЗЕМПЛЯРА с вызовом и получим результат ее работы
print(y.static_hello())  # --> static_hello

''' Проблема решена, у нас есть возможность вызывать функцию и от класса, и от экземпляра
    Удобно, когда нужна именно функция, и именно внутри класа
    
    Как сделать так, чтобы можно было так же вызывать метод, 
    чтобы и класс, и экземпляр автоматически подавались ему в аргумент? 
    Повесить другой декоратор @classmethod и задать аргумент cls '''

class Example3:

    def hello():
        print('hello')

    @staticmethod
    def static_hello():  # БЕЗ self
        print('static_hello')

    def instance_hello(self):
        print(f'instance_hello {self}')

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')

# Обратимся к функции ОТ КЛАССА с вызовом и получим принт и имя класса
print(Example3.class_hello())  # --> class_hello <class '__main__.Example3'>

y = Example3()
# Обратимся к функции ОТ ЭКЗЕМПЛЯРА с вызовом и получим принт и имя класса
print(y.class_hello())  # --> class_hello <class '__main__.Example3'>

''' Такие методы нужны, когда вы хотите делать обработку не над одним экземпляром, 
    а над целым классом, он доступен так как подается в переменную метода '''
