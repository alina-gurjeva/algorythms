"""4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""


def summ_progr_geom(b1, q, n):
    sum_n = b1 * (1 - q ** n) / (1 - q)
    return sum_n


n = int(input('Введите натуральное число: '))
b1 = 1
b2 = -0.5
q = b2/b1
sum_n = summ_progr_geom(b1, q, n)
print(sum_n)