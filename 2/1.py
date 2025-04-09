# https://inf-ege.sdamgia.ru/problem?id=72560

def func(x, y, w, z):
    f = (x <= (y <= z)) and (y <= (z == (not w)))
    if not f:
        print(x, y, w, z)


print("x y w z")
for x in [0, 1]:
    for y in [0, 1]:
        for w in [0, 1]:
            for z in [0, 1]:
                func(x, y, w, z)

# w z y x
