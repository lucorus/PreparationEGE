# https://inf-ege.sdamgia.ru/problem?id=27889

with open("27-B_demo.txt") as f:
    n = int(f.readline())

    sm = 0
    min_razn = 10 ** 5
    for i in range(n):
        a, b = [int(j) for j in f.readline().split()]
        sm += min(a, b)
        if abs(a-b) < min_razn and abs(a-b) % 3 != 0:
            """
            Если окажется, что сумма выбранных чисел (из каждой пары выбираем минимальное) делится на 3,
            то к итоговой сумме прибавим минимальную разницу между числами в паре, чтобы сумма не делилась на 3
            """
            min_razn = abs(a-b)

if sm % 3 == 0:
    print(sm + min_razn)
else:
    print(sm)