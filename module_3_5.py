#  #  РЕКУРСИЯ

#  # Задача "Рекурсивное умножение цифр":
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if number < 10:
        return first
    else:
        return first*get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(20304))
print(get_multiplied_digits(19670908))

# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
# print(summa(6))

# def recursion():  #  не указано, когда функция будет останавливаться
#     recursion()
#
# recursion()

# stack = []
# stack.append(1)
# print('Добавили элемент' , stack)
# stack.append(2)
# print('Добавили элемент' , stack)
# stack.append(3)
# print('Добавили элемент' , stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)


# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])
#     if number < 10:
#         return first
#     # elif first == 0:   #  Ведущие нули в десятичных целочисленных литералах не допускаются; используйте префикс 0o для восьмеричных целых чисел
#     #     first = int(str_number[1])
#     #     return first*get_multiplied_digits(int(str_number[2]))
#     else:
#         return first*get_multiplied_digits(int(str_number[1:]))
#
#
# #     print(str_number[0])

