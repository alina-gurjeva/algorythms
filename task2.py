# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def count_even_uneven(a):
    even = 0
    uneven = 0

    def _count_even_uneven(a):
        nonlocal even
        nonlocal uneven
        if a == 0:
            return
        a_rest = a % 10
        a = a // 10
        if a_rest % 2 == 0:
            even += 1
        else:
            uneven += 1
        return _count_even_uneven(a)

    _count_even_uneven(a)

    return even, uneven


a = int(input('Введите натуральное число: '))
even, uneven = count_even_uneven(a)
print(f'четных: {even}, нечетных: {uneven}')