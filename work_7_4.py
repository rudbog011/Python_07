print('Введите a:')
a = int(input())
print('Введите b:')
b = int(input())
if a > b:
    k = a
    a = b
    b = k
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)