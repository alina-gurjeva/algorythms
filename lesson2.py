# Ссылка на блок схему: https://drive.google.com/file/d/1YlTsqsjgEh8AyV-6AQsI7IsS0DUdCvNK/view?usp=sharing
# также прикладываю pdf.

# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random


def guess_num(attempts, x):
    if attempts == 0:
        print(f'Игра окончена! Ответ: {x}')
        return
    guess = int(input('Введите число: '))
    if guess > x:
        print('Больше!')
        return guess_num(attempts - 1, x)
    if guess < x:
        print('Меньше!')
        return guess_num(attempts - 1, x)
    if guess == x:
        print("Угадал")
        return


x = random.randint(0, 100)
attempts = 10
guess_num(attempts, x)

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

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

a = int(input('Введите натуральное число: '))  # строго говоря, в задании не конкретизировано, каким должно
# быть число. Если рассматривать вариант с вещественными числами - схема получится слишком громоздкой
# с учетом запрета на срезы и массивы, т.к. понадобится куча проверок и разветвлений алгоритма.
# Впрочем и это тоже реализуемо, напишите если задание интерпретировано неверно и надо рассмотреть
# всю числовую прямую - допишу.

while True:
    a_rest = a % 10
    if a_rest == 0:
        a = a // 10
    else:
        break


def reverse(a):
    if a == 0:
        return ""
    return f"{a%10}" + reverse(a//10)


a = reverse(a)
print(a)

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def summ_progr_geom(b1, q, n):
    sum_n = b1 * (1 - q ** n) / (1 - q)
    return sum_n


n = int(input('Введите натуральное число: '))
b1 = 1
b2 = -0.5
q = b2/b1
sum_n = summ_progr_geom(b1, q, n)
print(sum_n)


# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def sum_n1(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s


def sum_n2(n):
    return n*(n+1)/2


n = int(input('Введите число: '))

s1, s2 = sum_n1(n), sum_n2(n)

if s1 == s2:
    print('Равенство выполнено')
else:
    print('Равенство не выполнено')

# Возможен и рекурсивный вариант для sum_n1 (но возможно переполнение стека):


def sum_n1(n):
    if n == 1:
        return 1
    return n + sum_n1(n-1)


# можно проверить:
s1, s2 = sum_n1(n), sum_n2(n)
print(s1 == s2)

