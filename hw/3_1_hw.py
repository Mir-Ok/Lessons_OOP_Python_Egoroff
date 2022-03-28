class Person:

    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        print('getter called')
        return self.__gender

    @gender.setter
    def gender(self, value):
        # print('setter called')
        if value:
            if value == 'female':
                self.__gender = value
            elif value == 'male':
                self.__gender = value
            else:
                self.__gender = "male"
                print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
        else:
            self.__gender = "male"

    def __str__(self):
        if self.__gender == "female":
            return f'Гражданка {self.surname} {self.name}'
        else:
            return f'Гражданин {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"