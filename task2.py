"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.

ВНИМАНИЕ. Посколько в задаче не уточнено, i-е по счету начиная с 0 или с 1,
решение осуществлено исходя из предположения, что нумерация начинается с 1.
То есть, 3е по счету простое число будет равно 5."""

import math
import timeit
import cProfile
import seaborn as sns
import matplotlib.pyplot as plt


def test_prime_num(func):
    answers = {1: 2, 2: 3, 3: 5, 6: 13, 10: 29, 13: 41, 19: 67, 23: 83}
    for key in answers.keys():
        assert func(key) == answers[key], f'Error on {key} num: {func(key)} != {answers[key]}'
    print('All tests ok')


# Функция с решетом Эратосфена:
def eratosphen(i):
    """
    :param i:
    :return: i prime number
    """
    start_len = i*3

    def _eratosphen(array):
        m = 2
        n = len(array)
        while m < n:
            if array[m] != 0:
                j = m * 2
                while j < n:
                    array[j] = 0
                    j = j + m
            m += 1
        return [x for x in array if x != 0]
    while True:
        is_prime = [x for x in range(start_len)]
        is_prime[1] = 0
        primes = _eratosphen(is_prime)
        if len(primes) < i:
            start_len *= 2
        else:
            return primes[i-1]


# test_prime_num(eratosphen)

# timeit
t1 = timeit.timeit('eratosphen(50)', number=100, globals=globals())  # 0.0071544999999999526
t2 = timeit.timeit('eratosphen(100)', number=100, globals=globals())  # 0.015152799999999966
t3 = timeit.timeit('eratosphen(1000)', number=100, globals=globals())  # 0.40981999999999996
t4 = timeit.timeit('eratosphen(10000)', number=100, globals=globals())  # 4.537937299999999
print(t1, t2, t3, t4)


k_nums2 = [5, 9, 13, 17]
t_times2 = [t1, t2, t3, t4]
sns.lineplot(x=k_nums2, y=t_times2)

plt.show()  # only need for pycharm
# saved as eratosphen_prime.png

# cProfile:
cProfile.run('eratosphen(10000)')

"""
19 function calls in 0.054 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.054    0.054 <string>:1(<module>)
        1    0.000    0.000    0.053    0.053 task2.py:24(eratosphen)
        3    0.043    0.014    0.047    0.016 task2.py:31(_eratosphen)
        3    0.004    0.001    0.004    0.001 task2.py:41(<listcomp>)
        3    0.005    0.002    0.005    0.002 task2.py:43(<listcomp>)
        1    0.000    0.000    0.054    0.054 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Вывод:
# Скорость роста больше чем O(n^2), график (и скорость) больше похожи на факториальный рост.
# Поскольку внутренняя функция _eratosphen была вызвана 3 раза, значит для такого числа пришлось
# перестраивать массив с числами 2-жды (т.к. итоговый массив не содержал искомого числа.).
# Если увеличить стартовый массив, например start_len = i*4, то, конечно, на этом числе
# функция отработает быстрее, но на меньших числах - медленнее, поскольку будет заполнять слишком большой массив.
# Основная проблема реализации через решето: неизвестно заранее, какой длины массив создавать,
# т.к. при росте разрядов числа i, необходимая длина массива растет нелинейно.


# Алгоритм без использования решета
def find_prime(i):
    k_primes = 0
    current_num = 2

    def _is_prime(x):
        start_num = 2
        max_del = math.sqrt(x)+1
        is_prime = True
        for i in range(start_num, int(max_del)):
            if x % i == 0:
                is_prime = False
        return is_prime

    while True:
        if _is_prime(current_num) is True:
            k_primes += 1
        if k_primes == i:
            return current_num
        current_num += 1


# test_prime_num(find_prime)

# timeit
t1 = timeit.timeit('find_prime(50)', number=100, globals=globals())  # 0.014735300000000007
t2 = timeit.timeit('find_prime(100)', number=100, globals=globals())  # 0.04408610000000002
t3 = timeit.timeit('find_prime(1000)', number=100, globals=globals())  # 1.5666795
t4 = timeit.timeit('find_prime(10000)', number=100, globals=globals())  # 63.442302000000005
print(t1, t2, t3, t4)


k_nums2 = [5, 9, 13, 17]
t_times2 = [t1, t2, t3, t4]
sns.lineplot(x=k_nums2, y=t_times2)

plt.show()  # only need for pycharm
# saved as just_prime.png

# cProfile:
cProfile.run('find_prime(10000)')

"""
209460 function calls in 0.718 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.718    0.718 <string>:1(<module>)
        1    0.021    0.021    0.718    0.718 task2.py:100(find_prime)
   104728    0.683    0.000    0.697    0.000 task2.py:104(_is_prime)
        1    0.000    0.000    0.718    0.718 {built-in method builtins.exec}
   104728    0.014    0.000    0.014    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

# Вывод:
# Для поиска 10_000 числа понадобилось проверить 104_728 чисел. Каждая проверка содержит цикл
# до корня из этого числа элементов. То есть сложность, вероятно, близка к оценке: O(n^n)log(n),
# что значительно превышает скорость алгоритма с использованием решета Эратосфена.
# Для 10_000 числа разница 4.5 секунды простив 63.5
