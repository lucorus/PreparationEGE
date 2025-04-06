# возвращает кол-во методов, с помощью которых можно достичь переданного числа
def methods(num: int, start_num: int, numbers: list[int], commands: list[str], exclude: list[int] | None) -> int:
    # работает только если операций, по возвращению назад (деление или вычитание) нету
    if type(exclude) != list:
        exclude = []
    ans = 0
    for i in range(start_num, num):
        for operation in commands:
            if eval(str(i) + operation) == num:
                if i not in exclude:
                    ans += numbers[i]
    return ans


def func(start_num: int, end_num: int, exclude: list[int] | None, commands: list, include: list | None,
         numbers: list | None = None, base_cnt_variants=1) -> int:
    """
    :param start_num: число, от которого начитается отсчёт
    :param end_num: конечное число последовательности
    :param exclude: список чисел, которые нужно исключить из траектории
    :param commands: команды, которые нужно использовать для преобразования
    :param include: список чисел, которые обязательно должны быть в траектории вычисления
    :param numbers: список, в котором под каждым индексом написаны кол-во траекторий достижения числа
    :param base_cnt_variants: кол-во траекторий для получения start_num
    """
    numbers = [0 for i in range(0, end_num+1)] if not numbers else numbers
    numbers[start_num] = base_cnt_variants
    for i in range(start_num + 1, end_num + 1):
        numbers[i] = methods(i, start_num, numbers, commands, exclude)
        try:
            if i in include:
                include.pop(0)
                return func(i, end_num, exclude, commands, include, numbers, numbers[i])
        except:
            pass
    print(numbers)
    print(f"answer = {numbers[-1]}")
    return numbers[-1]


# https://inf-ege.sdamgia.ru/problem?id=59728
func(3, 18, [13], ["+1", "+2", "*3"], [8])

# https://inf-ege.sdamgia.ru/problem?id=13418
func(1, 27, [26], ["+1", "*2+1"], None)

# https://inf-ege.sdamgia.ru/problem?id=29129
func(3, 60, None, ["+1", "*2"], [13, 30])


# не подходит для задач типа: https://inf-ege.sdamgia.ru/problem?id=55610
