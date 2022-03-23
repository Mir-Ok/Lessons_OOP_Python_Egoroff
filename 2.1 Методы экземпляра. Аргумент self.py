class Cat:

    def hello():
        print('Hello world from Kitty')

'''  При вызове функции через класс - работает, через созданный экземпляр класса - нет '''

print(Cat.hello())  # -->  Hello world from Kitty None

bob = Cat()
# print(bob.hello())  # --> ОШИБКА hello() takes 0 positional arguments but 1 was given

print(bob.hello)    # -->  <bound method Cat.hello of <__main__.Cat object at 0x000002791518B040>>

print(type(Cat.hello()))  # --> ФУНКЦИЯ <function Cat.hello at 0x00000222EFE758B0>
print(type(bob.hello))    # --> МЕТОД   <bound method Cat.hello of <__main__.Cat object at 0x00000222EFD27400>>

''' В чем отличие обычной функции и метода?
    1. М - это Ф, объявленная внутри класса
    2. М связан с конкретным оюъектом (могу вызвать только через обращение к объекту), Ф - нет, ее можно вызвать отдельно
    3. При вызове М, объект, с которым он связан автоматически проставляется в аргумент функции, в скобки. Хорошо понять
     через сортировку списка, например, потому что если a.sort(), то сортируется именно а, не какой-то другой.

    '''

# Закрепим пункт 3, добавим в функцию hello() при объявлении агрумент *args.
# Выведем этот аргумент чтобы показать, какой объект берет метод при исполнении
# Адрес памяти совпадает

class Cat:

    def hello(*args):
        print('Hello world from Kitty', args)

jim = Cat()
print(jim.hello()) # --  Hello world from Kitty <__main__.Cat object at 0x000001D4C0332640>
print(jim)  # -- >                              <__main__.Cat object at 0x000001D4C0332640>

bob = Cat()
print(bob.hello()) # --  Hello world from Kitty <__main__.Cat object at 0x000001F2C9CF7400>
print(bob)  # -- >                              <__main__.Cat object at 0x000001F2C9CF7400>

# Обратите внимание на разницу адресов экземпляров!

# Метод обязательно связывается сам с объектом, к которому применяется.


''' Через объект, который попадает первым аргументом внутрь метода,  можно получить
    доступ к атрибутам класса (добавим породу и метод ее показа)

    '''


class Cat:

    def hello(*args):
        print('Hello world from Kitty', args)

    breed = 'pers'

    def show_breed(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        print(f'my breed is {instance.breed}')

    # добавим функцию для вывода метода
    def show_name(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        print(f'my name is {instance.name}')

Walt = Cat()
print(Walt.show_breed())  # --> my breed is pers вызвали исходное
print(Walt.__dict__)  # --> {} у экземпляра атрибутов нет

# Изменим породу
Walt.breed = 'siam'

print(Walt.show_breed())  # --> my breed is siam вызвали новое, теперь это атрибут экземпляра, а не класса
print(Walt.__dict__)  # --> {'breed': 'siam'} у экземпляра появился атрибут

Fox = Cat()
print(Fox.show_breed())  # --> my breed is pers вызвали исходное, оно не изменилось

''' Можем аналогично выводить имя, т.е. сначала создадим атрибут, а потмо его вызовем '''
Mary = Cat()
print(Mary.show_name())  # --> nothing
Mary.name = 'www'  # создаем аттрибут на лету
print(Mary.show_name())  # --> my name is www

''' Для создания атрибута можно тоже воспользоваться методом '''


# Введем изначальную проверку на наличие аттрибута

class Cat:

    def hello(*args):
        print('Hello world from Kitty', args)

    breed = 'pers'

    def show_breed(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        print(f'my breed is {instance.breed}')

    # добавим проверку наличия имени
    def show_name(instance):  # instance - экземпляр класса, к которому применим, см. ниже
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')

''' Чтобы создавать атрибуты внутри класса, а не вне его, добавим метод set_value '''

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

    def set_value(koshka, value, age=0):  # вместо self не суть важно что писать, это первый аттрибут
                  koshka.name = value
                  koshka.age = age  # атрибут класса приравнивается к аргументу функции

Tom = Cat()  # --> пока у тома есть только порода
Tom.show_name()  # --> nothing

Tom.set_value('TOM')  # --> не вызывается без как минимум одного параметра
Jerry = Cat()
Jerry.set_value('JERRY', 15)  # значение возраста по умолчанию изменится

''' Аргумент self 
    В Питоне принято сам объект так называть при создании метода, поэтому вместо inctance и koshka должно быть self '''