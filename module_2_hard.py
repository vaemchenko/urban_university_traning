# n = 9

# ДЗ Старый шифр модуль 2

import random
num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(num)
a = list()
list_pass = str()
for i in range(3,n//2+1):
    if n % i == 0:
     a.append(i)
a.append(n)
for j in range(2,n-1):
    for i in a:
        if j <= i//2 and j != i:
            list_pass += f"{i}{j}"

b = a[-1::]
print(*b)
print(list_pass)

# num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for i in num:
#     print(i)
