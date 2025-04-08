# https://inf-ege.sdamgia.ru/problem?id=38604

with open("27_B(2).txt") as f:
    n = int(f.readline())
    nums = [int(i) for i in f.readlines()]

sums = [0 for i in range(n)]  # список для хранения суммы чисел
sums[0] = nums[0]
min_len = 10 ** 5
mx_sum = 0

# Словарь для хранения индексов остатков (ключ - остаток, а значение - индекс)
# сохраняется первый попавшийся остаток
remainder_index = dict()

for i in range(1, n):
    current_ost = (sums[i-1] + nums[i]) % 43
    sums[i] = sums[i-1] + nums[i]

    if current_ost % 43 == 0:
        if mx_sum < sums[i]:
            mx_sum = sums[i]
            min_len = i + 1
        elif mx_sum == sums[i]:
            min_len = min(min_len, i + 1)

    # Проверка остатков
    if current_ost in remainder_index:
        index_ost = remainder_index[current_ost]
        potential_sum = sums[i] - sums[index_ost]
        if mx_sum < potential_sum:
            mx_sum = potential_sum
            min_len = i - index_ost
        elif mx_sum == potential_sum:
            min_len = min(min_len, i - index_ost)
    else:
        remainder_index[current_ost] = i  # Сохраняем индекс, если остаток не встречался

print(min_len)
