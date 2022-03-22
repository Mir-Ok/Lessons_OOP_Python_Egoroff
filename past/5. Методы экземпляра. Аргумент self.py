class Cat:
    def hello(*args):
        print('Hello world from Kitty', args)

'''  При вызове функции через класс - работает, через созданный экземпляр класса - нет

Cat.hello()  -->  Hello world from Kitty

bob = Cat()
bob.hello()  --> hello() takes 0 positional arguments but 1 was given

'''
bob = Cat()

print(Cat.hello)  # --> ФУННКЦИЯ <function Cat.hello at 0x00000222EFE758B0>
print(bob.hello)  # --> МЕТОД <bound method Cat.hello of <__main__.Cat object at 0x00000222EFD27400>>

''' В чем отличие обычной функции и метода?
    1. М - это Ф, объявленная внутри класса
    2. М связан с конкретным оюъектом (могу вызвать только через обращение к объекту), Ф - нет, ее можно вызвать отдельно
    3. При вызове М, объект, с которым он связан автоматически проставляется в скобки. Хорошо понять через сортировку
       списка, например, потому что если a.sort(), то сортируется именно а, не какой-то другой
    
    '''

# закрепим пункт 3, добавим в функцию hello() при объявлении агрумент *args.
# Выведем этот аргумент чтобы показать, какой объект берет метод при исполнении
# Адрес памяти совпадает

jim = Cat()
print(jim.hello()) # --  Hello world from Kitty <__main__.Cat object at 0x000001D4C0332640>
print(jim)  # -- >                              <__main__.Cat object at 0x000001D4C0332640>

print(bob.hello()) # --  Hello world from Kitty <__main__.Cat object at 0x000001F2C9CF7400>
print(bob)  # -- >                              <__main__.Cat object at 0x000001F2C9CF7400>


''' Через объект, который попадает первым аргументом внутрь метода,  можно получить
    доступ к атрибутам класса (добавим породу и метод ее показа)
    
    '''
class Cat:
    breed = 'pers'
    def hello(*args):
        print('Hello world from Kitty', args)

    def show_breed(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        print(f'my breed is {instance.breed}')

    # добавим функцию для вывода метода
    def show_name(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')

Walt = Cat()
print(Walt.show_breed())  # --> my breed is pers вызвали исходное
print(Walt.__dict__)  # --> {} у экземпляра атрибутов нет

Walt.breed = 'siam'
print(Walt.show_breed())  # --> my breed is siam вызвали новое, теперь это атрибут экземпляра, а не класса
print(Walt.__dict__)  # --> {'breed': 'siam'} у экземпляра появился атрибут

Fox = Cat()
print(Fox.show_breed())  # --> my breed is pers вызвали исходное, оно не изменилось

''' Можем аналогично выводить имя, т.е. сначала создадим атрибут, а потмо его вызовем
    '''
Mary = Cat()
print(Mary.show_name())  # --> nothing
Mary.name = 'www'  # создаем аттрибут на лету
print(Mary.show_name())  # --> my name is www

''' Для создания атрибута можно тоже воспользоваться методом 
    '''

class Cat:
    breed = 'pers'
    def hello(*args):
        print('Hello world from Kitty', args)

    def show_breed(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        print(f'my breed is {instance.breed}')

    # добавим функцию для вывода метода
    def show_name(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')

    def set_value(koshka, value, age=0):  # не суть важно что писать, это первый аттрибут,
                                   # который принимает агрумент, к кот. вызван метод?
                                   # и передадим параметр
        koshka.name = value
        koshka.age = age  # не путать метод и атрибут класса

Tom = Cat()  # --> пока у тома ест только порода
Tom.show_name()  # --> nothing

Tom.set_value('TOM')  # --> первый параметр не передаем, подставится автоматически
                      # совсем без параметров тоже нельзя

''' Добавим аргумент по умолчанию age = 0 '''

Jerry = Cat()
Jerry.set_value('JERRY', 15)


''' Что такое self?

    Вместо instance или koshka можно поставить что угодно, но в Питоне принято тот объект, от
    которого был вызван метод называть self 
    
    Поэтому при создании метода внутри класса в скобках сразу создается self, программа помогает
    '''

class Cat:
    breed = 'pers'
    def hello(*args):
        print('Hello world from Kitty', args)

    def show_breed(self):  # instance - экземпляр класса, к которому применим, см. ниже
        print(f'my breed is {self.breed}')

    # добавим функцию для вывода метода
    def show_name(self):  # instance - экземпляр класса, к которому применим, см. ниже
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')

    def set_value(self, value, age=0):  # не суть важно что писать, это первый аттрибут,
                                   # который принимает агрумент, к кот. вызван метод?
                                   # и передадим параметр
        self.name = value
        self.age = age  # не путать метод и атрибут класса