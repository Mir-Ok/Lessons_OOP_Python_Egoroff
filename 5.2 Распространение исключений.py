''' Когда программа линейная, то идет работа до воврата исключения.
    А как все устроено. когда нелинейно и есть функция? '''

def first():
    print('start first')
    print('finish first')

# print('hello')
# first()

''' hello
    start first
    finish first   '''


''' Вспомним про стек и области видимости 
    То есть мы идем по стеку, глобально, запускаем функцию - уходим в нее локально, по
    ее окончанию снова выходим в глобал 
    Добавим заведомое исключение и посмотрим, какой будет отчет:
    
    1. cначала он укажет на ту строку, которая вызывает косячную функцию, 
    2. далее указывает на косяк уже внутри функции
    3. после сам тип ошибки '''


def first():
    print('start first')
    # 1/0
    print('finish first')

# print('hello')
# first()

''' hello
    start first
    Traceback (most recent call last):
      File "D:/1_Python/ООП на Python (Egoroff)/5.2 Распространение исключений.py", line 27, in <module>
        first()
      File "D:/1_Python/ООП на Python (Egoroff)/5.2 Распространение исключений.py", line 23, in first
        1/0
    ZeroDivisionError: division by zero
    '''

''' Усложним ситуацию и вложим функцию 
    Стек: main --> first --> second '''

def first():
    print('start first')
    second()
    print('finish first')

def second():
    print('start second')
    1/0
    print('finish second')

# print('hello')
# first()

''' В отчете мы увидим, что сначала указывает на first, потом на second, затем на
    косячную строку в second и последним тип ошибки.
    Успеет отработать первая часть first, перейти в second, отработать половину там
    и вернуть исключение.
    
    То есть оно распространяется обратно по стеку вызова, причем на каждом шаге проверяет 
    наличие try-except 
    И ищем мы в отчете снизу вверх
    
        Traceback (most recent call last):
      File "D:/1_Python/ООП на Python (Egoroff)/5.2 Распространение исключений.py", line 59, in <module>
        first()
      File "D:/1_Python/ООП на Python (Egoroff)/5.2 Распространение исключений.py", line 50, in first
        second()
      File "D:/1_Python/ООП на Python (Egoroff)/5.2 Распространение исключений.py", line 55, in second
        1/0
    ZeroDivisionError: division by zero
    hello
    start first
    start second
    '''

# Добавим обработку исключения

def first():
    print('start first')
    second()
    print('finish first')

def second():
    print('start second')
    try:
        1/0
    except ZeroDivisionError:
        print('handling')
    print('finish second')

# print('hello')
# first()

''' hello
    start first
    start second
    handling
    finish second
    finish first  '''

# Либо мы можем добавить выше по стеку обработку функции с возможным исключением

def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('handling')
    print('finish first')

def second():
    print('start second')
    1/0
    print('finish second')

print('hello')
first()

''' hello
    start first
    start second
    handling
    # --- finish second этого нет в выдаче, функция после исключения выходит наверх, не дорабатывает
    finish first  '''

# Исключение будет подниматься выше по стеку жо тех пор, пока не встретить обработку исключения и тогда все
# кончится мирно, либо дойдет до конца стека и тогда будет прерывание работы кода