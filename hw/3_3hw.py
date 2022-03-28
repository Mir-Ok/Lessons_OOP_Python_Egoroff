class Vector:

    def __init__(self, *args):
        val = []
        [val.append(i) for i in args if isinstance(i, int)]
        self.values = sorted(val)

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(self.values)}'
        else:
            return f'Пустой вектор'

    def __add__(self, other):

        # если other число
        if isinstance(other, int):
            new_val = []
            for i in range(len(self.values)):
                new_val.append(self.values[i] + other)
            return Vector(*new_val)

        # если other вектор
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):  # длины векторов равны
                new_val = [self.values[i] + other.values[i] for i in range(len(self.values))]
                return Vector(*new_val)

            else:  # длины векторов НЕ равны
                return f'Сложение векторов разной длины недопустимо'

        else:  # если НЕ число и НЕ вектор
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):

        # если other число
        if isinstance(other, int):
            new_val = []
            for i in range(len(self.values)):
                new_val.append(self.values[i] * other)
            return Vector(*new_val)

        # если other вектор
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):  # длины векторов равны
                new_val = [self.values[i] * other.values[i] for i in range(len(self.values))]
                return Vector(*new_val)

            else:  # длины векторов НЕ равны
                return f'Сложение векторов разной длины недопустимо'

        else:  # если НЕ число и НЕ вектор
            print(f'Вектор нельзя сложить с {other}')

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"


# ------------- Вариант 2 -----------------
class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if type(i) == int])

    def __str__(self):
        return f'Вектор{tuple(self.values)}' if self.values != [] else 'Пустой вектор'

    def __add__(self, x):
        if type(x) != int and type(x) != Vector:
            print(f'Вектор нельзя сложить с {x}')
        else:
            if type(x) == int:
                return Vector(*[i + x for i in self.values])
            elif type(x) == Vector and len(x.values) == len(self.values):
                return Vector(*[self.values[i] + x.values[i] for i in range(0, len(self.values))])
            else:
                print("Сложение векторов разной длины недопустимо")

    def __mul__(self, x):
        if type(x) != int and type(x) != Vector:
            print(f'Вектор нельзя умножить на {x}')
        else:
            if type(x) == int:
                return Vector(*[i * x for i in self.values])
            elif type(x) == Vector and len(x.values) == len(self.values):
                return Vector(*[self.values[i] * x.values[i] for i in range(0, len(self.values))])
            else:
                print("Умножение векторов разной длины недопустимо")