"""1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их."""

import timeit
import cProfile
import seaborn as sns  # just my preference
import matplotlib.pyplot as plt

# Буду рассматривать следующую задачу со 2го урока:
"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


# Тест для проверки функций:
def test_even_uneven_func(func):
    nums = [1, 10, 222, 12345, 5555]
    answers = [(0, 1), (1, 1), (3, 0), (2, 3), (0, 4)]
    for ind, num in enumerate(nums):
        even, uneven = func(nums[ind])
        assert (even, uneven) == answers[ind], f"Error on {ind} pos"
    print('all tests ok!')


# Первое решение было таким (рассматриваем сам алгоритм, без ввода пользователем данных):
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


# test_even_uneven_func(count_even_uneven)

# timeit
t1 = timeit.timeit('count_even_uneven(12345)', number=1000, globals=globals())  # 0.000930699999999951
t2 = timeit.timeit('count_even_uneven(12345_6789)', number=1000, globals=globals())  # 0.001558999999999977
t3 = timeit.timeit('count_even_uneven(12345_6789_8765)', number=1000, globals=globals())  # 0.0022786000000000195
t4 = timeit.timeit('count_even_uneven(12345_6789_8765_4321)', number=1000, globals=globals())  # 0.0030158999999999603
print(t1, t2, t3, t4)


k_nums = [5, 9, 13, 17]
t_times = [t1, t2, t3, t4]
sns.lineplot(x=k_nums, y=t_times)

plt.show()  # only need for pycharm
# saved as func_1.png

# Посмотрим также cProfile:
n = 123456789764321*99999999999999999999999999999999999999999999999999999
cProfile.run('count_even_uneven(n)')  # для наглядности увеличим число

"""
73 function calls (5 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:28(count_even_uneven)
     69/1    0.000    0.000    0.000    0.000 task1.py:32(_count_even_uneven)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Выводы:
# Алгоритм был реализован в виде рекурсивной функции без кеша.
# Алгоритм показал линейную сложность O(n) (по графику).
# По результатам CProfile даже при очень большом числе время исполнения меньше 1/1000 секунды,
# максимальная нагрузка ложится на функцию _count_even_uneven, которая при длине числа в 68 цифр вызывается
# 69 раз.


# Второе решение реализуем через цикл:
def count_even_uneven2(a):
    even = 0
    uneven = 0
    while True:
        if a == 0:
            break
        a_rest = a % 10
        a = a // 10
        if a_rest % 2 == 0:
            even += 1
        else:
            uneven += 1
    return even, uneven


# test_even_uneven_func(count_even_uneven2)

# timeit
t1 = timeit.timeit('count_even_uneven2(12345)', number=1000, globals=globals())  # 0.00047360000000007396
t2 = timeit.timeit('count_even_uneven2(12345_6789)', number=1000, globals=globals())  # 0.0008285000000000098
t3 = timeit.timeit('count_even_uneven2(12345_6789_8765)', number=1000, globals=globals())  # 0.0012704999999999522
t4 = timeit.timeit('count_even_uneven2(12345_6789_8765_4321)', number=1000, globals=globals())  # 0.0017163999999999513
print(t1, t2, t3, t4)


k_nums2 = [5, 9, 13, 17]
t_times2 = [t1, t2, t3, t4]
sns.lineplot(x=k_nums2, y=t_times2)

plt.show()  # only need for pycharm
# saved as func_2.png
# cProfile:
cProfile.run('count_even_uneven2(n)')

"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:93(count_even_uneven2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
# Выводы:
# Время исполнения оказалось на порядок быстрее. Сложность осталась O(n).
# Количество вызовов функций сократилось с 73 до 4. Т.к. вместо очередного вызова функции
# в этом алгоритме происходила очередная итерация.


# Третье решение реализуем через строки, уменьшив количество вычислений
def count_even_uneven3(a):
    even_nums = {'0', '2', '4', '6', '8'}
    even = 0
    uneven = 0
    a = str(a)
    for element in a:
        if element in even_nums:
            even += 1
        else:
            uneven += 1
    return even, uneven


# test_even_uneven_func(count_even_uneven3)

# timeit
t1 = timeit.timeit('count_even_uneven3(12345)', number=1000, globals=globals())  # 0.0005196999999999008
t2 = timeit.timeit('count_even_uneven3(12345_6789)', number=1000, globals=globals())  # 0.0006521999999999917
t3 = timeit.timeit('count_even_uneven3(12345_6789_8765)', number=1000, globals=globals())  # 0.0007975000000000065
t4 = timeit.timeit('count_even_uneven3(12345_6789_8765_4321)', number=1000, globals=globals())  # 0.0009375999999999829
print(t1, t2, t3, t4)


k_nums3 = [5, 9, 13, 17]
t_times3 = [t1, t2, t3, t4]
sns.lineplot(x=k_nums3, y=t_times3)

plt.show()  # only need for pycharm
# saved as func_3.png
# cProfile:
cProfile.run('count_even_uneven3(n)')

"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task1.py:145(count_even_uneven3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Выводы:
# Время снова улучшилось. Особенно заметна разница на наибольшем из чисел: 0.00094 против 0.00168.
# Алгоритм остался линейным O(n).
# Результаты по cProfile остались прежними. Такие результаты можно объяснить тем, что проверка числа на наличие
# в множестве - это одна операция (константное время), тогда как если идти циклом по числу, то требуется 3
# операции (константное время каждая) (взять остаток %10, взять деление нацело //10, взять остаток от деления на 2).

# В заключение, посмотрим тайминги 2х последних функций на действительно большом числе (длина числа 95439 цифр)
# (1ю функцию не рассматриваем из-за максимальной глубины рекурсии):
big_num = 123456789764321*9**10000

t2 = timeit.timeit('count_even_uneven2(big_num)', number=100, globals=globals())  # 2.9569437
t3 = timeit.timeit('count_even_uneven3(big_num)', number=100, globals=globals())  # 0.1608494
print(t2)
print(t3)
# Почти 3 секунды против 0.16 секунды. 3й алгоритм оказался самым быстрым.
