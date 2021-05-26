print('Введите количество натуральных чисел n:')
n = int(input())
flag = 0
print('Введите', n, 'чисел:')
for i in range(n):
    number = int(input())
    if number % 2 != 0:
        flag = 1
if flag == 1:
    print('YES')
else:
    print('NO')
       