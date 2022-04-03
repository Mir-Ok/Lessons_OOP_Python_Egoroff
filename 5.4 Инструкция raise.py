''' Инструкция raise позволяет возбуждать исключения в любой строчке кода

    Важно, что после ключевого слова raise мы можем только писать классы исключений

    '''

# cоздадим переменную и поместим в нее исключение
a = TypeError('Ошибка типа')
print(a.args)  # --> ('Ошибка типа',)
print(a)       # --> Ошибка типа

# в момент инициализации у экземпляра создаются аргументы .args

''' Мы можем вызвать ошибку и тем самым сразу уронить весь код, если обработка
    такого типа исключений не прописана '''

# ошибку можно возбуждать и через обращение к переменной

# raise a  # --> TypeError: Ошибка типа

# иногда ошибку надо перехватить, вывести и потом снова вывести
# в чем нам поможет сохранение исключения в переменную

''' Если мы хотим обработать несколько исключений, а вывести 
    информацию только о последнем - from none '''

# try:
#     raise ValueError('Ошибка значения')
# except ValueError:
#     try:
#         raise TypeError('Ошибка типа')
#     except TypeError:
#         raise Exception('Большое исключение')

# по коду выше при запуске получим весь стек исключений

''' Пример кода с указанием что выводить
    Причем если мы напишем from second - мы получим все, а если 
    from first, то только часть, т.к. счет идет от ошибки вверх по коду '''
try:
    raise ValueError('Ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from None