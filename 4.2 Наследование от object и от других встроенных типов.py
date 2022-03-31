''' Вспомним, что в Питоне любое значение является объектом
    Даже экземпляры встроенных типов, например, int(), он наследует от базового класса object
    '''

print(issubclass(int, object))  # --> True
print(issubclass(dict, object))  # --> True

''' Важно понимать, что самый первый созданный класс, который явно ни от кого не наследует, 
    на самом деле наследуется от базового класса object  '''

class Person:  # равноценно  class Person(object):
    pass

print(issubclass(Person, object))  # --> True

''' Как это знание нам поможет? Если мы вызовем dir() к object, то увидим список его методов
    и узнаем, какие методы доступны нашему классу по дефолту и соотв. экземплярам этого класса '''

print(dir(object))
''' ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
    '__format__',     '__ge__', '__getattribute__', '__gt__', 
    '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__'] '''

class MyList(list):
    pass

m_list = MyList()
print(m_list)  # --> [] это происходит потому что это экземпляр класса, наследующего list
               # сразу рождается списком, плюс в доступе все методы списка доступны через .

               # но он не прямой потомок list(), он его внук, потому что есть класс MyList()

class MyDict(dict):
    pass

m_dict = MyDict()
print(m_dict)  # --> {}