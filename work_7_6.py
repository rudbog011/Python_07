print('Введите натуральное число n:')
n = int(input())
s = 0
for i in range(n + 1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        s += i
print(s)
