''' Что такое объект в программировании? Это контейнер, состоящий из данных (атрибутов) и поведения (матодов) объекта.

     Например, создадим список a = [1,2,3] и для него возможно поведение a.sum(), оно же метод списка. Но для строки
     такое поведение уже невозможно. '''
# Локальное изменение

# Каждый объект принадлежит какому-то типу:
a = [1, 2, 3]
print(type(a))  # --> <class 'list'>

# Есть функция проверки принадлежности объекта выбранному классу
print(isinstance(4, float))  # --> False, так как не вещественное

print(isinstance(4, object))  # --> True, так как в Питоне все объект
print(isinstance(a, object))  # --> True, так как в Питоне все объект
print(isinstance(list, object))  # --> True, так как в Питоне все объект

''' Что такое класс? Это шаблон для создания объектов, причем они сразу же наделяются определенным поведением.
    Например, списки получают все свои методы и свойства. 
    
    Аналогично встроенным, мы можем создавать свои классы и их экземпляры. '''

class Car:
    pass

# создадим экземпляр класса
b = Car()
print(isinstance(b, Car))  # --> True, так как в b объект класса Car

# создадим еще один экземпляр. Он аналошичен первому, но занимает другое место в памяти
d = Car()

# Изменим класс, и это изменит и его экземпляры, они станут появляться сразу с набором свойств
class Car2:
    model = 'BMW'
    engine = 1.6

f = Car2()
print(f.model)  # --> BMW

