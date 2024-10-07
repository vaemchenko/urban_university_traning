value_list = [1, 'red', [5, 6, 7]]
value_dict = {'a':True, 'b':'black', 'c':[11, 22, 33]}
value_list_2 = [[103, '104', False], 'braun']

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b=25)
print_params(c = [1,2,3])
print_params()
print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2, 42)

print()

def append_to_list(item, list_my=None):
  if list_my is None:
   list_my = []
  list_my.append(item)
  print(list_my)
  print(*list_my)

append_to_list('str')
append_to_list(77)
append_to_list([11, 22, 33, 44, 55, True, 'abd'])
append_to_list({'a':1, 'b':2, 'c':False})