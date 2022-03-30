class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)


v1 = Vector(1, 2, 4, 8)
print(v1)  # --> [1, 2, 4, 8]
print(v1.values)  # --> [1, 2, 4, 8]

''' В данном случае экземпляр класса - это коллекция, 
    а к ее элемантам можно обращаться по индексу. Но не в случае экземпляра
    По умолчанию, индексирование не поддерживается 
    
    Создадим его '''


class Vector2:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    # задаем обработку подаваемого в [] при вызове экземпляра класса, например val[1]
    def __getitem__(self, item):
        if 0 <= (len(self.values)):
            return self.values[item]
        else:
          raise IndexError('Индекс за границами наше коллекции')

    # добавим операцию изменения по индексу
    def __setitem__(self, key, value):
        if 0 <= (len(self.values)):
            self.values[key] = value
        else:
          raise IndexError('Индекс за границами наше коллекции')

    # добавим операцию удаления по индексу
    def __delitem__(self, key):
        if 0 <= (len(self.values)):
            del self.values[key]
        else:
          raise IndexError('Индекс за границами наше коллекции')

''' Немного поиграем и заменим начало индексации с 0 до 1 '''

class Vector3:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    # задаем обработку подаваемого в [] при вызове экземпляра класса, например val[1]
    def __getitem__(self, item):
        if 1 <= (len(self.values)):
            return self.values[item-1]
        else:
          raise IndexError('Индекс за границами наше коллекции')

    # добавим операцию изменения по индексу
    def __setitem__(self, key, value):
        if 1 <= key <= (len(self.values)):
            self.values[key-1] = value
        # добавим расширение списка другим списком и новое обращение
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0]*diff)
            self.values[key] = value
        else:
          raise IndexError('Индекс за границами наше коллекции')

    # добавим операцию удаления по индексу
    def __delitem__(self, key):
        if 0 <= (len(self.values)):
            del self.values[key]
        else:
          raise IndexError('Индекс за границами наше коллекции')

''' Еще один способ использовать __setitem__ - создание разреженных списков.
    То есть если у нас 3 элемента в списке, и мы хотим получить восьмой, 
    то нам нужно часть позиций забить нулями '''

class Vector4:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    # задаем обработку подаваемого в [] при вызове экземпляра класса, например val[1]
    def __getitem__(self, item):
        if 1 <= (len(self.values)):
            return self.values[item-1]
        else:
          raise IndexError('Индекс за границами наше коллекции')

    # добавим операцию изменения по индексу
    def __setitem__(self, key, value):
        if 0 <= key <= (len(self.values)):
            self.values[key] = value
        else:
          raise IndexError('Индекс за границами наше коллекции')

    # добавим операцию удаления по индексу
    def __delitem__(self, key):
        if 0 <= (len(self.values)):
            del self.values[key]
        else:
          raise IndexError('Индекс за границами наше коллекции')