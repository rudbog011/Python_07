print('Введите натуральное число n:')
n = int(input())
m = 1 #Произведение и флаг в одной переменной
for i in range(n + 1):
    if i % 10 == 2 or i % 10 == 9:
        m *= i
if m == 1:
    print('0')
else:
    print(m)
