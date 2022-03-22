# Если у класса есть метод, например:

class Cat():
    breed = 'pers'
    def set_value(self, value, age = 5):
        self.name = value
        self.age = age

# ... то мы можем создать экземпляр класса и дополнить его описание этим методом

vov = Cat()
vov.set_value('vov', 8)

print(vov.name)  # --> vov

''' Можно сделать удобнее, при помощи магического метода __init__
    Который принимает на вход наш новосоздаваемый объект
    '''

class Cat():
    breed = 'pers'
    def set_value(self, value, age = 5):
        self.name = value
        self.age = age

    def __init__(self):  # вызывается после создания объекта, когда его пространство имен уже существует
        print('hello new object is ', self)

''' Чтобы насытить информацией класс, можем задать волшебному методу аргументы '''

class Cat():
    # breed = 'pers' убираем, так как перенесли ниже
    def set_value(self, value, age = 5):
        self.name = value
        self.age = age

    def __init__(self, name, breed = 'pers', age = 1, color = 'white'):
        print('hello new object is ', self)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

got = Cat('got')  # --> при создании подаем один обязательный аргумент,
                  # именованные могут остаться по умолчанию
                  # справа в консоли отразятся все аргументы
