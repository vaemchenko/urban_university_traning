# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
# ВОПРОС как пренебречь регистром строки

calls = 0

def count_call():
    global calls
    calls+=1

def string_info(a):
    count_call()
    a == str()
    return (len(a), a.upper(), a.lower())


def is_contains(string, list_to_search):
    count_call()
    for i in list_to_search:
         if string.lower() == i.lower():
             return True
    return False



print(string_info('Conducktor'))
print(string_info('Armavir'))
print(is_contains('street', ['1', '2', 'st', 'allo', 'StreT']))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('MOSCOW', ['Piter', 'MoscOW', 'lonDon', 'urBAN', 'SPB']))
print(calls)


# string_info('Forex')
#
# a = 'Urban'
#
# print((len(a), a.upper(), a.lower() ))
#
# def is_contains(a,b):
#     a = str()
#     b = list()
#     if a in b == True:
#         print(True)
#     else:
#         print(False)
#
# is_contains(a='st', b=[1, 2, 'st', 'allo'])


# calls = 0
#
# def count_call():
#     global calls
#     calls+=1
#
# def string_info(a):
#     a == str()
#     print(len(a), a.upper(), a.lower())
#     count_call()
#
# def is_contains(string, list_to_search):
#     string.lower()
#     for i in list_to_search:
#         n=0
#         i[n].lower()
#         n+=1
#         i[n].lower()
#     if string in i:
#         print(True)
#         count_call()
#     else:
#         print(False)
#         count_call()
#
# string_info('Conducktor')
# is_contains('st', [1, 2, 'st', 'allo'])
# is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
# string_info('Armavir')
# is_contains('Eva', ['Dan', 'Lena', 'Alex', 'Eva'])
# print(calls)
