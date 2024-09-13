# phone_book = {'Denis': 88003332211, 'Max': 88003332212, 'Stas': 88003332213, 'Lara': 88003332214} # для создания словаря ИСПОЛЬЗУЕМ {} В паре 'ключ': значение '' не изменный объект
# print(phone_book)
# print(type(phone_book))
# print(phone_book['Stas']) # вводим ключ - получаем значение, значение можно менять
# phone_book['Stas'] = 99003332213 # не забываем '' для ключа
# print(phone_book)
# phone_book['Anton'] = 88003332215 # добавление пары в словарь
# print(phone_book)
# del phone_book['Max'] # del удаление пары из словаря
# print(phone_book)
# phone_book.update({'Saha': 77003332216, 'Masha':77003332217, 'Alex': 77003332217}) # .update обновляет словарь (слияние словарей)
# print(phone_book)
# print(phone_book.get('Denis')) # .get выводит значение 'ключа"
# print(phone_book.get('Kamila')) # нет ключа в словаре - выводит None
# print(phone_book.get('Kamils', 'Такого ключа нет')) # None можно изменить
# print(phone_book)
# phone_book.pop('Alex') # .pop удаляет ключ из словаря
# print(phone_book)
# a = phone_book.pop('Masha') # извлечение пары из словаря или списка
# print(a)
# list_ = [1, 2, 3, 4, 5]
# print(list_)
# list_.pop(0)
# print(list_)
# print(phone_book.keys())  # .keys извлекает коллекцию ключей из словаря
# print(phone_book.values())  # .values извлекает значенияиз словаря
# print(phone_book.items())  # .items извлекает попарно ключи и значения
# phone_book.update({'Saha': 88003332216,
#                    'Stas': 88003332213})  # .update можно менять значения в парах, ключ не измененяем
# print(phone_book)
# set_ = {1, 2, 3, 4, 1, 2, 3, 4, 5, True, 'String', (1, 2, 3)} # множество хранит только уникальные значения разных типов
# print(set_)
# list_ = [1, 1, 1, 1, 2, 3, 4, 5]
# print(list_)
# print(set(list_))  # set переводит во множество
# print(list_.remove(5)) # .discard .remove удаля.т элемент, но .discard не выводит ошибку, если элемента нет забываем сделать второй вывод (print)
# print(list_)
from os import remove

my_dict = {'Anton': 1999, 'Masha': 2003, 'Roma': 1970,  'Lara': 2000, 'Alex': 1960, 'Marta': 1945}
print(my_dict)
print(type(my_dict))
print(my_dict['Marta'])
print(my_dict.get('Denis'))
my_dict.update({'Denis': 2001, 'Nike': 1974})
print(my_dict)
a = my_dict.pop('Anton')
print(a)
print(my_dict)
my_set = [1, 1, 2, 3, True, 'Sky', '55']
print(my_set)
print(type(my_set))
print(set(my_set))
print(type(set(my_set)))
ours_set = set(my_set)
print(ours_set)
ours_set.update({77, 'river'})
print(ours_set)
print(ours_set.remove('55'))
print(ours_set)