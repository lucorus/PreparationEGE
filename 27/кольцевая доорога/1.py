with open("107_27_A.txt") as f:
    n = int(f.readline())
    cnt_trash = [int(i) for i in f.readlines()]

# считаем сумму для первого элемента
right_sum = sum(cnt_trash[0:n//2])
left_sum = sum(cnt_trash[n//2:])

for i in range(1, n):
    if i < n // 2:
        # i * 3 - расстояние до пункта
        right_sum += cnt_trash[i] * i * 3
    else:
        left_sum += cnt_trash[i] * (n - i) * 3
summ = left_sum + right_sum  # сумма доставки мусора, если пункт находится на первой позиции

for i in range(2, n):
    if i < n // 2:
        # i * 3 - расстояние до пункта
        right_sum -= cnt_trash[i] * 1 * 3  # вычитаем стоимость за перевоз мусора из пункта справа в прошлом варианте
        right_sum += cnt_trash[i-1] * 1 * 3
    else:
        left_sum -= cnt_trash[i] * (n - i) * 3

