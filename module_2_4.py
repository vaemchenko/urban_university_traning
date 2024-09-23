# Block_0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15:
#     print(i)
#     print('ok')

# Block_1
# currency = ['eur', 'gbp', 'chf', 'cad', 'aud', 'nzd', 'meh', 'rur', 'jpy', 'her']
# for i in currency:
#     print(i[0])
#     print(i[1])
#     print(i[2])
#     if i[0] == 'h' or i[1] == 'h' or i[2] == 'h': # условие вывода "ok", когда выводимое значение включает в себя h #
#         print('ok')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in numbers:
    if i == 1:
        continue
    f = True
    for j in range(2, i):
        if (i % j == 0):
            not_prime.append(i)
            f = False
            break
    if f:
        prime.append(i)
print(prime)
print(not_prime)



