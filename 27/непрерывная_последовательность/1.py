"""
https://inf-ege.sdamgia.ru/problem?id=38961
Может показаться, что нужно найти сумму непрерывной последовательности, в которой все числа чётные, но на самом деле
нужно найти сумму последовательности, в которой кол-во чётных чисел кратно 10, а нечётных хоть сколько.
то есть:
[2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 101, 101, 2, 2, 1, 2]
в таком случае нужно найти сумму последовательности:
[2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 101, 101]
"""

with open('27-B.txt') as f:
    n = int(f.readline())
    nums = [int(i) for i in f.readlines()]

evens = [0]

for i in range(n):
    if nums[i] % 2 == 0:
        # получаем список индексов чётных элементов
        evens.append(i)
evens.append(0)

mx = 0
cnt_evens = len(evens)
for i in range(0, cnt_evens % 10 - 1):
    start_index = evens[i] + 1
    stop_index = evens[ i + cnt_evens - (cnt_evens % 10)  + 1]
    summ = sum(nums[start_index:stop_index])
    mx = max(summ, mx)

print(mx)


