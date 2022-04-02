class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.my_gender = gender  # my_gender по названию сеттера

    @property
    def my_gender(self):
        print('getter called')
        return self.gender

    @my_gender.setter
    def my_gender(self, value):
        # print('setter called')
        if value:
            if value == 'female':
                self.gender = value
            elif value == 'male':
                self.gender = value
            else:
                print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
                self.gender = "male"

        else:
            self.gender = "male"

    def __str__(self):
        if self.gender == "female":
            return f'Гражданка {self.surname} {self.name}'
        else:
            return f'Гражданин {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"
print(p3.__dict__)