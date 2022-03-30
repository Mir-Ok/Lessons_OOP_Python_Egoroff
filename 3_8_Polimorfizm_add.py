from Polimorfizm_3_8 import Rectangle

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)

# print(rect1.get_rect_area(), rect2.get_rect_area())


from Polimorfizm_3_8 import Square

sq1 = Square(3)
sq2 = Square(12)

# print(sq1.get_square_area(), sq2.get_square_area())

''' Пока мы испортируем и вроде все хорошо 

    Соберем в коллекцию наи фигуры, пройдем по списку циклом и посчитаем площади
    Обратим внимание, что иной раз площадь квадрата, иной раз п/у 
    
    Если к квадрату вызвать метод для треугольника - ошибка, наоборот соотв.
    Можно в цикле ввести проверку на фигуру, и пока классов немного, это решение работает 
    
    А если добавим круг? Код станет слишком большим 
    А если добавятся еще проверки внутри?
    '''

from Polimorfizm_3_8 import Surcle

su1 = Surcle(3)
su2 = Surcle(12)

figures = [rect1, rect2, sq1, sq2, su1, su2]

# for fiqure in figures:
#     if isinstance(fiqure, Rectangle):
#         print(fiqure.get_rect_area())
#     if isinstance(fiqure, Square):
#         print(fiqure.get_square_area())
#     if isinstance(fiqure, Surcle):
#         print(fiqure.get_surcle_area())

''' 12
    60
    9
    144
    28.26
    452.16
    '''

'''  
    
    Нужно решение, чтобы с одной стороны работать с объектами одинаково,
    а с другой, чтобы каждый из них вел себя по-разному 
    
    Здесь поможет полиморфизм - обработка разных объектов методом с одним названием 
    
    Удивительно, но замена названий методов на один решает вопрос. Причем сам Питон уже при получении
    объекта будет определять, что именно применить, оно будет зависеть от самого класса
     
    То есть мы закладываем полиморфизм в момент создания экземпляра, и после при вызове метода
    Питон сам обратится к соотв. классу, найдет там этот метод. Название метода одно, 
    а привязка экземпляра к разным классам, а в разных классах разная логика работы метода '''

for fiqure in figures:
    print(fiqure.get_area())

''' 12
    60
    9
    144
    28.26
    452.16
    '''

''' Чтобы активизировать полиморфное поведение экземпляров класса,
    мы можем прописать метод __str__, и тогда при вызове на печать
    мы увидим все тоже разное поведение одного метода
    '''

for fiqure in figures:
    print(fiqure, fiqure.get_area())

''' Rectangle sides = 3, 4 12
    Rectangle sides = 12, 5 60
    Square sides = 3 9
    Square sides = 12 144
    Surcle radius = 3 28.26
    Surcle radius = 12 452.16
    '''