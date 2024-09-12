# food = ["apple", "coconut", "banana"] # создаем список
# print(food[1])
# food[1] = "peach" # выбираем эдемент из списка по порядковому номеру
# print(food)
# food.append(True) # добавляем в список элемент
# print(food)
# food.extend("string") # добавляем в список строку
# print(food)
# food.extend(["string", 2]) # добавляем  в список список
# print(food)
# food.remove("apple") # удаляем элемент из списка
# print(food)
# print(2 in food) # проверить наличие элемента в списке
# print("g" not in food) # проверить отсутствие элемента в списке
# print(food[0:9:3]) # срезы в списке позволяют работать как и со строками

# tuple_ = 1, 2, 3, 4 # 1 способ написания кортежа
# tuple_1 = (1, 2, 3, 4) # 2 способ написания кортежа
# tuple_2 = tuple([1, 2, 3, 4]) # 3 способ написания кортежа
# print(tuple_)
# print(tuple_1)
# print(tuple_2)
# print(type(tuple_2))
# print(type(tuple_))
# tuple_ = (1, 2, 3, 4, True, "String", [20, 21, 22, 23])   # кортеж может состоять из элементов, строк и списков
# tuple_11 = 1, 2, 3, 4, True, "String"
# list_11 = [1, 2, 3, 4, True, "String"]
# print(tuple_)
# print(tuple_[:7:2])
# print(tuple_11.__sizeof__())  #  команда sizeof - показывает сколько занято памяти
# print(list_11.__sizeof__())   # кортеж занимает пямяти меньше чем список
# tuple_ = ([1, 2, 3, 4], 0) + (11, 22, 33, 44) # КОКАТЕНАЦИЯ
# print(tuple_)
# tuple_[0][0] = 12 # сложение элементов (первого в строке и в кортеже)?
# print(tuple_)
# tuple_ = (1, 2) * 3 # умножение кортежа
# print(tuple_)
# immutable_var = (1, 2, True, "String", [0, 21, 22, 23])
# print(immutable_var)
# immutable_var[1] = 5 #Eror: 'tuple' object does not support item assignment В кортеже заменить элемент нельзя
immutable_var = 1, 2, 3, True, "string"
print(immutable_var)
print(type(immutable_var))
# immutable_var[2] = 0
# print(immutable_var) # ошибка поскольку <class 'tuple'>
currencies = ["eur", "gbp", "chf", "usd", "aud"]
print(currencies)
print(type(currencies))
mutable_list = currencies
currencies[4] = "nzd"
print(mutable_list)
currencies_1 = currencies + ["zar", "jpy"]
print(currencies_1)
mutable_list = currencies_1 * 2
print(mutable_list)
currencies_2 = currencies_1 + [1, 2]
print(currencies_2)
print(type(currencies_2))