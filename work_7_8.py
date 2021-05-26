print('Введите количество натуральных чисел n ≥ 2:')
n = int(input())
if n < 2:
    print('Неверное число')
else:
    print('Введите', n, 'чисел:')
    n_max = int(input())
    n_min = n_max
    for i in range(n - 1):
        n = int(input())
        if n > n_max:
            n_max = n
        elif n < n_min:
            n_min = n
    print('Минимум равен', n_min)
    print('Максимум равен', n_max)