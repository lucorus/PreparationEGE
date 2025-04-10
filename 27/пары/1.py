"""
https://inf-ege.sdamgia.ru/problem?id=48448
"""

with open("27-B.txt") as f:
    n = f.readline()

    """
    Создаём двумерный массив: 
    индексы в подмассивах - степень, в которую нужно возвести 2, чтобы получить данное число 
    (под индексом 0 хранятся нечётные числа)
    индекст подмассива - остаток от деления на 3 числа.
    
    В подмассивах записывается количество элементов в каждой группе
    """
    arr = [[0]*11 for i in range(3)]

    nums = []
    for i in f.readlines():
        x = int(i)
        j = x % 3
        k = 0
        while x % 2 == 0:
            x = x // 2
            k += 1
            if k == 10:
                # если k равно 10 => произведении с другим числом однозначно будет делиться на 1024 (2^10)
                break
        arr[j][k] += 1

ans = 0

"""
считаем кол-во чисел, делящихся на 3 без остатка и дающих при произведении степень 2 большую или равную 10
(учитываются числа только с разной степенью)
"""
for i in range(len(arr[0])):
    for j in range(max(i+1, 10-i)):
        if i + j >= 10 and i != j:
            ans += arr[0][i] * arr[0][j]

"""
считаем кол-во чисел, делящихся на 3 без остатка и дающих при произведении степень 2 большую или равную 10
(учитываются числа только с одинаковой степенью)
"""
for i in range(5, len(arr[0])):
    # вычитаем 1, чтобы при переборе вариантов не смотреть на вариант, где парой является текущее число с само собой
    # (для того же делим на 2)
    ans += (arr[0][i] * (arr[0][i] - 1)) // 2

"""
считаем кол-во чисел, делящихся на 3 с остатком 1 и 2 (при сложении будут делиться на 3 без остатка) и дающих при 
произведении степень 2 большую или равную 10
"""
for i in range(len(arr[1])):
    for j in range(len(arr[2])):
        if i + j >= 10:
            ans += arr[1][i] * arr[2][j]

print(ans)

